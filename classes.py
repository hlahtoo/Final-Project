import csv
from string import digits, ascii_letters

ALL_LETTERS_DIGITS = digits + ascii_letters
KEY = '9TUw5BcdL2kFAlezQs7PH6boIuJ3RiGxMprEmaN8Sh4gtO1WyqKZXnYDVv0Cfj'

class patient:
    """
    Patient class have first name, last name, age, gender, date of birth and visit summaries of the patient.
    
    It prints the name, age, gender, and date of birth in a nicely formatted string,
    has different methods.
    1. name() - a method that returns the first and last name of the patient
    2. add_visit_manually() - a method that allows you to add the visit summary by input
    3. add_visit_as_dict() - a method that allows you to add the visit summary with the dict with all the info
    4. display_general_info() - a method that displays the name, age, gender, date of birth of the patient
    5. display_all_info() - a method that displays all infos of the patients
    6. f_name_w_last_ini() - a method that returns first name with last name initial and ended with .csv
    7. display_as_list() - a method that returns the list that includes first name, last name, age, gender, dob and firstname with lastname initial.
    8. 
    """
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
    
    def display_general_info(self):
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"age : {self.__age}")
        print(f"Gender : {self.__gender}")
        print(f"Date of Birth: {self.__date_of_birth}")
        print('--------------------------------------------')
    
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
            print('-'*50)

    def f_name_w_last_ini(self):
        return self.__first_name + self.__last_name[0] +  ".csv"
    
    def display_as_list(self):
        first_name_w_l_ini = self.f_name_w_last_ini()
        return [self.__first_name, self.__last_name, self.__age, self.__gender, self.__date_of_birth, first_name_w_l_ini]

    def __str__(self) -> str:
        string = f"{self.__first_name} {self.__last_name}, {self.__age}, {self.__gender}, {self.__date_of_birth}"

        return string

class hospitalRecord:
    def __init__(self, name, patients =[]):
        self.name = name
        self.__patients = patients.copy()

    @property
    def patients(self):
        return self.__patients

    def add_patient(self, person: patient):
        """
        Adds patient to hospital record data
        """
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
    
    def patient_by_index(self, index: int):
        if index >= len(self.__patients):
            raise IndexError("Index out of range")
        else:
            return self.__patients[index]
    
    def size(self):
        return len(self.__patients)
    
    def __str__(self) -> str:
        return f"{self.name} ({self.size()} patients)"

class AdminAccount:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password       

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




def login():
    """function for login
    """
    print("Log in to your account")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    loaded_accounts = load_accounts('account.csv')
    account_matched = False
    for acc in loaded_accounts:
        #print(acc.username, acc.password)
        if username == acc.username and password == acc.password:
            account_matched = True
        """
        else:
            
            return login()"""
    if not account_matched:
        print("Username or password is incorrect! Please enter again")
        return login()
    else:
        return account_matched
    


def split_str(msg: str, lst: list) -> list[str]:
    """
    Split the string and add each of the letter in the list.
    For Example:
        >>> split_str("abc", lst)
        [a, b, c]
    Args:
        msg (str) : msg to split
        lst (list) : list that the splitted msg will be added
    Returns:
        lst[str] : list with msg elements
    """
    # use for loop to loop through the msg and append the lst
    for i in range(len(msg)):
        lst.append(msg[i])
    return lst


def add_str(lst: list) -> str:
    """
    Add the letters in the lst back together to create the string
    For Example:
        >>> add_str([a, b, c])
            abc
    Args:
        lst (list) : list that you want to create the string by adding 
                    together
    Returns:
        str: the convereted_msg (created by addng the elements in the list)
    """
    # create a empty string
    converted_msg = ''
    # add each element of the list one by one
    for i in lst:
        converted_msg += i
    return converted_msg


def change_letter(lst: list, key_for_index: str, key_for_change: str) -> list[str]:
    """
    Change or convert the elements in the list from one key to another
    i.e, can convert from ALL_LETTER_DIGITS to RANDOMKEY or
    from RANDOMKEY to ALL_LETTER_DIGITS
    For Example:
        >>> change_letter(["a", "b", "c"], "abc", "def" )
            ["d", "e", "f"]
        >>> change_letter(["b", "a", 1], "abc", "def")
            ["e", "d", 1]
    Args:
        lst (lst): list of elements to convert 
        key_for_index (str): the key string to get the index from
        key_for_change (str): the key that will be used to convert
    Returns:
        list : the list with the converted elements
    """
    for i in range(len(lst)):
        # use count function to check if the element will be in key_for_index
        if key_for_index.count(lst[i]) > 0:
            # get the index from key_for_index related to element
            index_key = key_for_index.index(lst[i])
            # change the element in accordance with the related index
            lst[i] = key_for_change[index_key]
        else:
            # if element doesnt exist in key_for_index, skip
            pass
    return lst

def encrypt(msg: str, key: str = KEY) -> str:
    """
    Convert the string in msg to encrypted msg using the key
    For Example:
        >>> encrypt("abc", "3WcqHN64fwYOuheZ2B9axvmr7RLT5i08snCFpoSAdKztJXIGEMUVgPkQjDl1by")
            "YOu"
    Arguments:
        msg (str) : the string that you want to encrypt or convert
        key (str) : the key that will be used for encryption
    Returns:
        str : encrypted or converted string using the key provided
    """
    # create an empty list to add the converted letter
    lst = []
    # split the msg and add them to the list
    split_str(msg, lst)
    # Encrypting each letter in the list using change_letter function
    change_letter(lst, ALL_LETTERS_DIGITS, key)
    # create the str by adding the elements in the list and return
    return add_str(lst)


def decrypt(msg, key) -> str:
    """
    Convert the encrypted str in msg to decrypted msg using the key
    For Example:
        >>>decrypt("YOu", "3WcqHN64fwYOuheZ2B9axvmr7RLT5i08snCFpoSAdKztJXIGEMUVgPkQjDl1by")
            "abc"
    Arguments:
        msg (str) : the string that you want to decrypt
        key (str) : the key that will be used to decrypt the msg
    Returns:
        Str : Decrypted string using the key provided
    """
    # create an empty list to add the converted letter
    lst = []
    # Split the msg and add them to the list
    split_str(msg, lst)
    # Decrypting each letter in the list using change_letter func
    change_letter(lst, key, ALL_LETTERS_DIGITS)
    # create the str by adding the elements in the list and return
    return add_str(lst)


def load_accounts(filename):
    key = '9TUw5BcdL2kFAlezQs7PH6boIuJ3RiGxMprEmaN8Sh4gtO1WyqKZXnYDVv0Cfj'
    lst = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            decrypt_user = decrypt(row['username'], key)
            decrypt_pw = decrypt(row["password"], key)
            lst.append(AdminAccount(decrypt_user, decrypt_pw))
    return lst

"""
a = patient('Hla', "Htoo", "24", "Male", "04/06/1233")
a.add_visit_manually("04/09/2023", "102/70", 98, 83, 87, "Headache/ Nasuea", "Nambudiri", "Drink more water")
a.add_visit_manually("04/09/2024", "103/70", 97, 84, 100, "Pelvis Pain", "Nambudiri", "Please get CT done for pelvis area")

v = patient('Srija', "Ga", "24", "Male", "04/06/1233")
v.add_visit_manually("04/09/2023", "102/70", 98, 83, 87, "Headache/ Nasuea", "Nambudiri", "Drink more water")
v.add_visit_manually("04/09/2024", "103/70", 97, 84, 100, "Pelvis Pain", "Nambudiri", "Please get CT done for pelvis area")


John_hopkhins = hospitalRecord("John Hopkins")
John_hopkhins.add_patient(a)
John_hopkhins.add_patient(v)
if None:
    print(John_hopkhins.find_patient('hla htoo'))"""