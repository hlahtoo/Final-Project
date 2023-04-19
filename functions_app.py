from enum import Enum
import sys
import classes
from typing import Tuple
from string import punctuation, digits, ascii_letters


class ViewOptionsAdmin(Enum):
    """ The options for the admin's view """
    EXIT = 1
    LOAD = 2
    CREATE = 3
    LIST = 4
    ADD = 5
    ADDVISIT = 6
    REMOVE = 7
    VIEW = 8
    NEWACCOUNT = 9
    CHANGEACCOUNT = 10
    SAVE = 11
    UNKNOWN = 12


def print_menu() -> None:
    """ Print the menu """
    print('Type any of the following commands. You can also type the number.')
    print('1. Exit - exit the program. It will save the list if one is loaded')
    print('2. Load - load a record from a file.')
    print('3. Create - Create a new hospital record')
    print('4. List - list the patients in the hospital record (if a list has been loaded)')
    print('5. Add - Add a patient to the hospital record')
    print("6. Add Visit - Add a visit summary to patient's data in the hospital record (if a patient exists)")
    print('7. Remove -  Remove a patient from the hospital record')
    print('8. View - View the patient record (general info and visit summaries)')
    print('9. New Account -  Create a new admin account')
    print('10. Change Account -  Log in to a different account')
    print('11. Save - save the list to a file.')


def print_welcome() -> None:
    """ Print the welcome message """
    print('Welcome to the hospital management tool')
    print('Type "help" to get a list of commands.')
    print()


def print_goodbye() -> None:
    """ Print the goodbye message """
    print('Goodbye! Thank you for using our app!')
    print('Have a nice day!')


def print_error(message: str) -> None:
    """ Print an error message
    Args:
        message (str): error message to print
    """
    print(f'Error: {message}', file=sys.stderr)

     
def get_filename() -> str:
    """ Get the filename from the user
    Returns:
        str: filename
    """
    filename = input('Enter a filename: ').strip()
    if filename.endswith('.csv'):
        return filename
    else:
        print_error('Filename must end with .csv')
        return get_filename()


def get_record_name() -> str:
    """ Get the list name from the user. 
    The name may not contain any punctuation or spaces.
    Returns:
        str: list name
    """
    name = input('Enter a list name: ').strip()
    if any(char in name for char in punctuation) or ' ' in name:
        print_error('List name may not contain punctuation or spaces')
        return get_record_name()
    else:
        return name


def get_hospital_name() -> str:
    """ Get the list name from the user. 
    The name may not contain any punctuation or spaces.
    Returns:
        str: list name
    """
    name = input('Enter a list name: ').strip()
    if any(char in name for char in punctuation) or ' ' in name:
        print_error('List name may not contain punctuation or spaces')
        return get_hospital_name()
    else:
        return name


def get_add_info() -> Tuple[str, str]:
    """ Get the information for adding a todo item
    Returns:
        tuple: (name, description)
    """
    first_name = input('Enter the first name of the patient: ').strip()
    last_name = input('Enter the last name of the patient: ').strip()
    age = input('Enter the age of the patient: ').strip()
    gender = input('Enter the gender of the patient: ').strip()
    dob = input('Enter the date of birth of the patient: ').strip()
    return (first_name, last_name, age, gender, dob)


def get_patient_info_for_visit(record: classes.hospitalRecord):
    """
    gets the patient from the record
    Args:
    record(hospitalRecord) : the record which includes the patient that you would like to get
    returns:
    the person(patient) : the patient that matches with the input name
    """
    first_name = input("Enter the first name of the patient: ")
    last_name = input("Enter the last name of the patient: ")
    name = f'{first_name} {last_name}'
    # find the patient using the name
    person = record.find_patient(name)
    #print(name, person)
    # if it is not found, it will return None
    if person == None:
        print("Patient not found!")
        # use recursion to get the name and search again
        return get_patient_info_for_visit(record)
    else:
        # if found, return the person
        return person
    

def get_add_visit_info():
    """
    gets the user input necessary to add the visit summary
    Returns:
    date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions
    """
    date = input('Enter the date of the visit: ').strip()
    blood_pressure = input('Enter the blood pressure of the patient: ').strip()
    temp = input('Enter the temperature of the patient: ').strip()
    pulse = input('Enter the pulse of the patient: ').strip()
    oxy_saturation = input('Enter the oxygen saturation of the patient: ').strip()
    symptoms = input('Enter the symptoms of the patient: ').strip()
    doctor = input('Enter the name of the doctor who saw the patient: ').strip()
    instructions = input('Enter the instructions of the doctor: ').strip()
    return (date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions)


def get_command_admin():
    """
    gets the input from the user and return the corresponding option
    returns:
    command that corresponds with the input
    """

    command = input('What would you like to do? ').strip().lower()
    if command == 'exit' or command == '1':
        return (ViewOptionsAdmin.EXIT)
    elif command == 'load' or command == '2':
        return (ViewOptionsAdmin.LOAD)
    elif command == 'create' or command == '3':
        return (ViewOptionsAdmin.CREATE)
    elif command == 'list' or command == '4':
        return (ViewOptionsAdmin.LIST)
    elif command == 'add' or command == '5':
        return (ViewOptionsAdmin.ADD)
    elif command == 'add visit' or command == '6':
        return (ViewOptionsAdmin.ADDVISIT)
    elif command == 'remove' or command == '7':
        return (ViewOptionsAdmin.REMOVE)
    elif command == 'view' or command == '8':
        return (ViewOptionsAdmin.VIEW)
    elif command == 'newaccount' or command == '9':
        return (ViewOptionsAdmin.NEWACCOUNT)
    elif command == 'changeaccount' or command == '10':
        return (ViewOptionsAdmin.CHANGEACCOUNT)
    elif command == 'save' or command == '11':
        return (ViewOptionsAdmin.SAVE)
    else:
        return (ViewOptionsAdmin.UNKNOWN)
