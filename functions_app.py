from enum import Enum
import sys
import classes
from typing import Tuple
from string import punctuation

class ViewOptions(Enum):
    """ The options for the view """
    EXIT = 1
    LIST = 2
    ADD = 3
    REMOVE = 4
    COMPLETE = 5
    SAVE = 6
    LOAD = 7
    NEW = 8
    UNKNOWN = 9

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

def print_list(hospital_record: classes.hospitalRecord) -> None:
    """ Print the list
    Args:
        todo_list (TodoList): list to print
    """
    print(hospital_record)
    for i in range(0, todolist.size()):
        print(f'{i+1}. {todolist.get_item(i)}')
        
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
    
def get_list_name() -> str:
    """ Get the list name from the user. 
    The name may not contain any punctuation or spaces.
    Returns:
        str: list name
    """
    name = input('Enter a list name: ').strip()
    if any(char in name for char in punctuation) or ' ' in name:
        print_error('List name may not contain punctuation or spaces')
        return get_list_name()
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

def get_add_visit():
    
    date = input('Enter the date of the visit: ').strip()
    blood_pressure = input('Enter the blood pressure of the patient: ').strip()
    temp = input('Enter the temperature of the patient: ').strip()
    pulse = input('Enter the pulse of the patient: ').strip()
    oxy_saturation = input('Enter the oxygen saturation of the patient: ').strip()
    symptoms = input('Enter the symptoms of the patient: ').strip()
    doctor = input('Enter the name of the doctor who saw the patient: ').strip()
    instructions = input('Enter the instructions of the doctor: ').strip()
    return (date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions)
