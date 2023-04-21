"""
Classes file for Patients' Management Portal
Name: Hla Htoo
Semester: Spring 2023
Course : CS5001
"""
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
    8. It prints in a nicely formatted string as well
    
    Attributes:
        firt_name (str) : the first name of the patient
        last_name (str) : the last name of the patient
        age (int) : the age of the patient
        gender (str) : gender of the patient
        date_of_birth (Str) : date of birth of patient
        visits (lst) : list of visit summaries of the patient
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
        """ Returns the first name of the patient"""
        return self.__first_name

    @property
    def last_name(self):
        """ Returns the last name of the patient"""
        return self.__last_name

    @property
    def age(self):
        """ Returns the age of the patient"""
        return self.__age

    @property
    def gender(self):
        """ Returns the gender of the patient"""
        return self.__gender

    @property
    def date_of_birth(self):
        """ Returns the date of birth of the patient"""
        return self.__date_of_birth

    def name(self):
        """ returns the first and last name of the patient"""
        return f"{self.__first_name} {self.__last_name}"

    def add_visit_manually(self, date:str, blood_pressure:str, temp:int, pulse:int, oxygen_saturation:int, symptoms:str, doctor_name:str, instructions:str):
        """
        add visit summmary manually as a dictionary to the list
        Args:
        date (str) : date of the visit
        blood_pressure (str) : blood pressure during visit
        temp (float) : temperature of the patient during visit
        pulse (int)  : pulse of the patient during visit
        oxygen_saturation (int) : oxygen saturation during visit
        symptoms (str) : symptoms during visit
        doctor (str) : name of the doctor who met the patient during visit
        instructions (str) : instructions from the doctor
        """
        # create an empty list
        visit = {}
        # added keys with their corresponding values in a nice format
        visit["date"] = date
        visit["blood_pressure"] = blood_pressure
        visit["temp"] = f"{temp} {chr(176)}F"
        visit["pulse"] = pulse
        visit["oxygen_saturation"] = f"{oxygen_saturation} %"
        visit["symptoms"] = symptoms
        visit["doctor"] = doctor_name
        visit["instructions"] = instructions
        # then add the updated dict to the "visits" list of the patient
        self.visits.append(visit)
    
    def add_visit_as_dict(self, visit: dict):
        """
        add the visit summary to "visits" list of the patient directly if the 
        visit summary is already a dict
        Args:
        visit (dict) : visit summary in dict data form that you want to add to the dict
        """
        # add the dict to the "visits" list of the patient
        self.visits.append(visit)
    
    def display_general_info(self):
        """print the general info of the patient in a nice format"""
        # print name
        print(f"Name: {self.__first_name} {self.__last_name}")
        # print age
        print(f"age : {self.__age}")
        # pring gender
        print(f"Gender : {self.__gender}")
        # print date of birth
        print(f"Date of Birth: {self.__date_of_birth}")
        print('--------------------------------------------')
    
    def display_all_info(self):
        """Print general info and all visit summaries in a nice format"""
        # print name
        print(f"Name: {self.__first_name} {self.__last_name}")
        # print age
        print(f"age : {self.__age}")
        # print gender
        print(f"Gender : {self.__gender}")
        # pritn date of birth
        print(f"Date of Birth: {self.__date_of_birth}")
        # loop through each of the visit in "visits" list of the patient
        for visit in self.visits:
            # print all the keys with their respective values
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
        """returns first name and last name's first initial with .csv added at the end """
        return self.__first_name + self.__last_name[0] +  ".csv"
    
    def display_as_list(self):
        """returns a list of first name, last name, age , gender , date of birth, and the result from f_name_w_l_ini function"""
        # get the first name and last name's first initial with .csv added at the end
        first_name_w_l_ini = self.f_name_w_last_ini()
        return [self.__first_name, self.__last_name, self.__age, self.__gender, self.__date_of_birth, first_name_w_l_ini]

    def __str__(self) -> str:
        """prints the patient object in a nicely formatted string"""
        string = f"{self.__first_name} {self.__last_name}, {self.__age}, {self.__gender}, {self.__date_of_birth}"

        return string

class hospitalRecord:
    """
    hospitalRecrod class have name,and a list of patients
    
    It prints the name, and the list of patients in a nicely formatted string,
    has different methods.
    1. add_patient(person) : adds person to the hospital record
    2. remove_patient(person) : removes the person from the hospital record
    3. find_patient(person) : finds the patient from the hospital record
    4. patient_by_index(index) : find the patient with the index
    5. size() : returns the total number of the patients

    Attributes:
        name (str) : the name of the hospital
        patients (lst) : list of the patients in the hospital
    """
    def __init__(self, name: str, patients:list =[]):
        self.name = name
        self.__patients = patients.copy()

    @property
    def patients(self):
        # returns the patients of the hospital
        return self.__patients

    def add_patient(self, person: patient):
        """
        Adds patient to hospital record data
        Args: person (patient) : person with patient class whom you want to add
        """
        # check first if person is actually patient
        if not isinstance(person, patient):
            # if not, then, raise error
            raise TypeError("Person has to be patient class")
        else:
            # if so, then add it to the list of patients
            self.__patients.append(person)

    def remove_patient(self, person: patient):
        """
        Removes patient from the hospital record
        Args:person (patient) : person with patient class whom you want to remove
        """
        # check first if person is actually patient
        if not isinstance(person, patient):
            # if not, then, raise error
            raise TypeError("Person has to be patient class")
        else:
            # if so ,remove from the list
            self.__patients.remove(person)

    def find_patient(self, name: str):
        """
        returns the first patient in the list that matches the name. 
        If no patient is found, it should return None. 
        Args: name (str) : name of the patient
        Returns: the patient whose name matches the name that is typed in
        """
        # loop through all the patients in the record
        for patient in self.__patients:
            # lowercase both the name that was typed in and the actual name of the paitnet and check
            if name.lower() == patient.name().lower():
                # if it matches, return the patient object
                return patient
        # if not, return None with the prompt
        print("There is no patient with the provided name at this hospital")
        return None
    
    def patient_by_index(self, index: int):
        """
        Finds and returns the patient by the index
        Args: index (int) : index where you want to find the patient
        Returns: the patient whom was found at the index
        """
        # if index is greater than the number of patients in the list, raise error
        if index >= len(self.__patients):
            raise IndexError("Index out of range")
        else:
            # if not, return the patient at the index
            return self.__patients[index]
    
    def size(self):
        """Returns the total number of patients in the record"""
        return len(self.__patients)
    
    def __str__(self) -> str:
        """prints the hospital record in a nicely formmated string"""
        return f"{self.name} ({self.size()} patients)"

class AdminAccount:
    """
    Admin account class has username and password.
    Attributes:
        username(str) : username of the account
        password(str) : password of the account
    """
    def __init__(self, username:str, password:str):
        self.__username = username
        self.__password = password
    
    @property
    def username(self):
        """returns the username of the account"""
        return self.__username
    
    @property
    def password(self):
        """returns the password of the account"""
        return self.__password       

def load_record_from_file(filename:str) -> None:
    """
    Loads the hospitalRecord from the file and returns the record
    Args:
    filename (str) : name of the file that you want to load the record from file
    """
    # remove the .csv from the filename to assign it to name variable
    name = filename[:-4]
    # create a hospitalRecord with that name
    hospital_record = hospitalRecord(name)
    # open the file that matches with the name and read each line
    with open(filename, 'r') as file:
        for line in file:
            # strip the line and split it by ',' and assign it to their respective variables
            f_name, l_name, age, gender, dob, fileforvisits = line.rstrip('\n').split(',')
            # create a patient object with the f_name, l_name, age, gender, and dob
            person = patient(f_name, l_name, age, gender, dob)
            # use the last variable "fileforvisits" from each line and open the filename with it
            with open(fileforvisits, 'r') as visit_file:
                # use csv.dictreader to read the file
                csv_file = csv.DictReader(visit_file)
                for row in csv_file:
                    # each row will become a dictionary if we use csv.dictreader and then adds the visits to the patient object
                    person.add_visit_as_dict(row)
                """for line in visit_file:
                    date, b_pressure, temp, pulse, oxy_saturation,symptoms, doctor,instruc = line.rstrip('\n').split(',')
                    person.add_visit_manually(date, b_pressure, temp, pulse, oxy_saturation,symptoms, doctor,instruc)"""
            # adds patients to the patient record
            hospital_record.add_patient(person)
    # returns the loaded hospitalRecord object
    return hospital_record

def save_record_to_file(record: hospitalRecord) -> None:
    """
    Saves the hospitalRecord object in csv files
    """
    # open or create the csv file with name of the record
    with open(f"{record.name}.csv", 'w', newline='') as file:
        # use csv.writer to write the file
        csvwriter = csv.writer(file)
        # for each person in the record
        for person in record.patients:
            # writerow() will write items in the list one after another separated by comma
            csvwriter.writerow(person.display_as_list()) # display_as_list() will return a list
            # gets first name with last name's initial
            first_name_w_l_ini = person.f_name_w_last_ini()
            # open or create the csv file with fisrt name with last name's initial name
            with open(first_name_w_l_ini, 'w', newline='') as file:
                # specifiy the field names
                field_names = ["date", "blood_pressure", "temp", "pulse", "oxygen_saturation",
                               "symptoms", "doctor", "instructions"]
                # with csv.DictWriter, assign field_names to the fieldnames in the csv file
                csv_visit_writer = csv.DictWriter(file, fieldnames=field_names)
                # then write the header row with writeheader() function
                csv_visit_writer.writeheader()
                # then for each visit in the list of visits for patients
                for visit in person.visits:
                    # write each row with writerow() function
                    csv_visit_writer.writerow(visit)




def login():
    """
    asks for username and password and then compares with the account in the file.
    If it finds the account, return True. If not, it will print "warning msg" and asks
    for the username and password again
    Returns: account_matched (Bool) : True if it mamtches
    """
    print("Log in to your account")
    # asks the user for username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # load accounts from account.csv
    loaded_accounts = load_accounts('account.csv')
    # create account_match vairable and sets it to False
    account_matched = False
    # loop through each account
    for acc in loaded_accounts:
        # checks if it matches with username and password
        if username == acc.username and password == acc.password:
            # if so, sets account_matched to True
            account_matched = True
    # if not call login() function again
    if not account_matched:
        print("Username or password is incorrect! Please enter again")
        return login()
    else:
        # if account matches, then return account_matched
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


def load_accounts(filename:str):
    """
    load accounts from the filename
    Args: filename where accounts are stored
    Returns: lst (list) : a list of accounts
    """
    # set the key for decryption
    key = '9TUw5BcdL2kFAlezQs7PH6boIuJ3RiGxMprEmaN8Sh4gtO1WyqKZXnYDVv0Cfj'
    # create a new list
    lst = []
    # open each filename as csvfile
    with open(filename, newline='') as csvfile:
        # use csv.DictReader to read the file
        reader = csv.DictReader(csvfile)
        # for each row in the file
        for row in reader:
            # row becomes a dictionary if we use DictReader()
            decrypt_user = decrypt(row['username'], key) # decrpt username using key
            decrypt_pw = decrypt(row["password"], key) # decrpt password using key
            # create AdminAccount with decrypted username and password and adds them to the list
            lst.append(AdminAccount(decrypt_user, decrypt_pw))
    # returns the list with the adminaccounts
    return lst

record = load_record_from_file('Testcase.csv')
print(record.patients[0].visits[0])