"""
Test file for patient Management Portal
Name: Hla Htoo
Course: CS5001
Semester: Spring 2023
"""
import unittest
import main
import classes
import functions_app

class TestPatient(unittest.TestCase):
    def test_str(self):
        """testing the person with patient class for string format"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        self.assertEqual(str(person), 'Hla Htoo, 24, male, 06/24/1998')
    
    def test_name(self):
        """testing the name function of patient class"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        self.assertEqual(person.name(), 'Hla Htoo')
    
    def test_add_visit_manually(self):
        """testing if we can add the visit summaries manually"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        person.add_visit_manually('04/20/2023', '120/70', 98, 107, 100, 'Chest Pain', "John", 'Get CT scan')

        visits = [{'date': '04/20/2023', 'blood_pressure': '120/70', 'temp': '98 °F',
                   'pulse': 107, 'oxygen_saturation': '100 %', 'symptoms': 'Chest Pain',
                   'doctor': 'John', 'instructions': 'Get CT scan'}]
        self.assertEqual(visits, person.visits)

    def test_add_visit_as_dict(self):
        """testing add_visit_dict if we can add the visit summary as a dict"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        visits1 = {'date': '04/20/2023', 'blood_pressure': '120/70', 'temp': '98 °F',
                   'pulse': 107, 'oxygen_saturation': '100 %', 'symptoms': 'Chest Pain',
                   'doctor': 'John1', 'instructions': 'Get CT scan'}
        person.add_visit_as_dict(visits1)
        visits2 = [{'date': '04/20/2023', 'blood_pressure': '120/70', 'temp': '98 °F',
                   'pulse': 107, 'oxygen_saturation': '100 %', 'symptoms': 'Chest Pain',
                   'doctor': 'John1', 'instructions': 'Get CT scan'}]
        self.assertEqual(visits2, person.visits)
    
    def test_f_name_w_last_ini(self):
        """testing f_name_w_last_ini function and if it returns the right string"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        correct_str = 'HlaH.csv'
        self.assertEqual(correct_str, person.f_name_w_last_ini())
    
    def test_display_as_list(self):
        """testing display_as_list function to see if it returns the same list"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        correct_list = ["Hla", "Htoo", 24, "male", "06/24/1998", "HlaH.csv"]
        self.assertEqual(correct_list, person.display_as_list())
    
class TestHospitalRecord(unittest.TestCase):
    def test_str(self):
        """testing string when hospitalRecord is created with no patients"""
        hospital = classes.hospitalRecord('Kaiser')
        correct_str = 'Kaiser (0 patients)'
        self.assertEqual(correct_str, str(hospital))
    
    def test_str1(self):
        """testing string when hospitalRecord is created with a patient"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person])
        correct_str = 'Kaiser (1 patients)'
        self.assertEqual(correct_str, str(hospital))
    
    def test_add_patient(self):
        """testing if add_patient function actually adds the patient to the record"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser')
        hospital.add_patient(person)
        correct_str = 'Kaiser (1 patients)'
        self.assertEqual(correct_str, str(hospital))
        self.assertEqual(person, hospital.patients[0])
    
    def test_remove_patient(self):
        """testing remove_patient function to see if it actually removes"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person])
        hospital.remove_patient(person)
        correct_str = 'Kaiser (0 patients)'
        self.assertEqual(correct_str, str(hospital))
    
    def test_find_patient(self):
        """testing find_patient with only one patient"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person])
        self.assertEqual(person, hospital.find_patient('Hla Htoo'))
    
    def test_find_patient2(self):
        """testing find_patient with two patients and lowercase name"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        person2 = classes.patient("Hla", "Htoo2", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person, person2])
        self.assertEqual(person2, hospital.find_patient('hla htoo2'))
        
    def test_find_patient3(self):
        """testing find_patient with wrong name"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        person2 = classes.patient("Hla", "Htoo2", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person, person2])
        self.assertEqual(None, hospital.find_patient('hla ht2o2'))
    
    def test_patient_by_index(self):
        """testing patient_by_index function with two patients and checking both"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        person2 = classes.patient("Hla", "Htoo2", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person, person2])
        self.assertEqual(person, hospital.patient_by_index(0))
        self.assertEqual(person2, hospital.patient_by_index(1))
    
    def test_size(self):
        """testing size function with 2 patients"""
        person = classes.patient("Hla", "Htoo", 24, "male", "06/24/1998")
        person2 = classes.patient("Hla", "Htoo2", 24, "male", "06/24/1998")
        hospital = classes.hospitalRecord('Kaiser', [person, person2])
        self.assertEqual(2, hospital.size())

class TestAdminAccount(unittest.TestCase):
    def test_adminaccount(self):
        acc = classes.AdminAccount('hlahtoo', 'cs5001')
        self.assertEqual('hlahtoo', acc.username)
        self.assertEqual('cs5001', acc.password)

class TestOthers(unittest.TestCase):
    def test_load_record_from_file(self):
        """testing load_record_from_file by comparing the strings after patients are loaded"""
        record = classes.load_record_from_file('Testcase.csv')
        person = classes.patient('test', '1', '24', 'M', "06/24/1233")
        self.assertEqual(str(person), str(record.patients[0]))
    
    def test_load_record_from_file2(self):
        """testing load_record_from_file by comparing the name of the record with 2 patients"""
        record = classes.load_record_from_file('Testcase.csv')
        self.assertEqual('Testcase (2 patients)', str(record))
    
    def test_load_record_from_file3(self):
        """testing load_record_from_file by comparing the visits"""
        record = classes.load_record_from_file('Testcase.csv')
        visits = {'date': '04/23/23', 'blood_pressure': '120/23', 'temp': '98 °F',
                  'pulse': '98', 'oxygen_saturation': '98 %', 'symptoms': 'chest pain',
                  'doctor': 'John', 'instructions': 'reduce stress'}
        print(record.patients[0].visits[0])
        self.assertEqual(visits, record.patients[0].visits[0])
    
    def test_handle_load(self):
        """testing handle_load function! Please type in "Testcase.csv" for filename"""
        record1 = classes.load_record_from_file('Testcase.csv')
        record = main.handle_load()
        self.assertEqual(str(record), str(record1))
        self.assertEqual(record.patients[0].visits[0], record1.patients[0].visits[0])
    
    def test_handle_load2(self):
        """testing handle_load function by comparing visits! Please type in "Testcase.csv" for filename"""
        record = main.handle_load()
        visits = {'date': '04/23/23', 'blood_pressure': '120/23', 'temp': '98 °F',
                  'pulse': '98', 'oxygen_saturation': '98 %', 'symptoms': 'chest pain',
                  'doctor': 'John', 'instructions': 'reduce stress'}
        self.assertEqual(visits, record.patients[0].visits[0])
    
    def test_create_new_record(self):
        """testing create_new_record. Please type in 'Kaiser'"""
        record = main.create_new_record()
        self.assertEqual('Kaiser (0 patients)', str(record))

        
    
if __name__ == '__main__':
  unittest.main(verbosity=2)

