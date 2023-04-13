import csv
class patient:
    def __init__(self, first_name, last_name,age, gender, date_of_birth, visits=[]) -> None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__gender = gender
        self.__date_of_birth = date_of_birth
        self.visits = visits.copy()

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @property
    def gender(self):
        return self.__gender

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    def name(self):
        return f"{self.__first_name} {self.__last_name}"

    def add_visit_manually(self, date, blood_pressure, temp, pulse, oxygen_saturation, symptoms, doctor_name, instructions):
        visit = {}
        visit["date"] = date
        visit["blood_pressure"] = blood_pressure
        visit["temp"] = f"{temp} {chr(176)}F"
        visit["pulse"] = pulse
        visit["oxygen_saturation"] = f"{oxygen_saturation} %"
        visit["symptoms"] = symptoms
        visit["doctor"] = doctor_name
        visit["instructions"] = instructions
        self.visits.append(visit)
    
    def add_visit_as_dict(self, visit: dict):
        self.visits.append(visit)
    
    def display_all_info(self):
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"age : {self.__age}")
        print(f"Gender : {self.__gender}")
        print(f"Date of Birth: {self.__date_of_birth}")
        for visit in self.visits:
            print("*"*50)
            print(f"         Summary of visit on " + visit["date"])
            print("You met with " + visit["doctor"])
            print("Blood Pressure: " + str(visit["blood_pressure"]))
            print("Temperature: " + str(visit["temp"]))
            print("Pulse: " + str(visit["pulse"]))
            print("Oxygen Saturation: " + str(visit["oxygen_saturation"]))
            print("Symptoms: " + visit["symptoms"])
            print("Instructions: " + visit["instructions"])

    def f_name_w_last_ini(self):
        return self.__first_name + self.__last_name[0] +  ".csv"
    
    def display_as_list(self):
        first_name_w_l_ini = self.f_name_w_last_ini()
        return [self.__first_name, self.__last_name, self.__age, self.__gender, self.__date_of_birth, first_name_w_l_ini]

    def __str__(self) -> str:
        string = f"{self.__first_name} {self.__last_name}, {self.__age}, {self.__gender}, {self.__date_of_birth}\n"

        return string

class hospitalRecord:
    def __init__(self, name, patients =[]):
        self.name = name
        self.__patients = patients.copy()

    @property
    def patients(self):
        return self.__patients

    def add_patient(self, person: patient):
        if not isinstance(person, patient ):
            raise TypeError("Person has to be patient class")
        else:
            self.__patients.append(person)

    def remove_patient(self, person: patient):
        if not isinstance(person, patient):
            raise TypeError("Person has to be patient class")
        else:
            self.__patients.remove(person)

    def find_patient(self, name: str):
        """
        returns the first item in the list that matches the short_name. 
        If no item is found, it should return None. If you are choosing to use 
        typing for a return type, you can use the optional typing syntax to indicate 
        that it can return None."""
        for patient in self.__patients:
            if name.lower() == patient.name().lower():
                return patient
        print("There is no patient with the provided name at this hospital")
        return None
    
    def size(self):
        return len(self.__patients)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.size()} patients)"
        

def load_record_from_file(filename:str):
    name = filename[:-4]
    hospital_record = hospitalRecord(name)
    with open(filename, 'r') as file:
        for line in file:
            f_name, l_name, age, gender, dob, fileforvisits = line.rstrip('\n').split(',')
            person = patient(f_name, l_name, age, gender, dob)
            with open(fileforvisits, 'r') as visit_file:
                csv_file = csv.DictReader(visit_file)
                for row in csv_file:
                    person.add_visit_as_dict(row)
                """for line in visit_file:
                    date, b_pressure, temp, pulse, oxy_saturation,symptoms, doctor,instruc = line.rstrip('\n').split(',')
                    person.add_visit_manually(date, b_pressure, temp, pulse, oxy_saturation,symptoms, doctor,instruc)"""

            hospital_record.add_patient(person)
    return hospital_record

def save_record_to_file(record: hospitalRecord) -> None:
    with open(f"{record.name}.csv", 'w', newline='') as file:
        csvwriter = csv.writer(file)
        for person in record.patients:
            csvwriter.writerow(person.display_as_list())
            first_name_w_l_ini = person.f_name_w_last_ini()
            with open(first_name_w_l_ini, 'w', newline='') as file:
                field_names = ["date", "blood_pressure", "temp", "pulse", "oxygen_saturation",
                               "symptoms", "doctor", "instructions"]
                csv_visit_writer = csv.DictWriter(file, fieldnames=field_names)
                csv_visit_writer.writeheader()
                for visit in person.visits:
                    csv_visit_writer.writerow(visit)

John = load_record_from_file("John.csv")
John.patients[0].display_all_info()

a = patient('Hla', "Htoo", "24", "Male", "04/06/1233")
a.add_visit_manually("04/09/2023", "102/70", 98, 83, 87, "Headache/ Nasuea", "Nambudiri", "Drink more water")
a.add_visit_manually("04/09/2024", "103/70", 97, 84, 100, "Pelvis Pain", "Nambudiri", "Please get CT done for pelvis area")

v = patient('Srija', "Ga", "24", "Male", "04/06/1233")
v.add_visit_manually("04/09/2023", "102/70", 98, 83, 87, "Headache/ Nasuea", "Nambudiri", "Drink more water")
v.add_visit_manually("04/09/2024", "103/70", 97, 84, 100, "Pelvis Pain", "Nambudiri", "Please get CT done for pelvis area")
#v.display_all_info()

John_hopkhins = hospitalRecord("John Hopkins")
John_hopkhins.add_patient(a)
John_hopkhins.add_patient(v)

#save_record_to_file(John_hopkhins)
J = load_record_from_file("John Hopkins.csv")
J.patients[0].display_all_info()