"""
Main file for Patients' Management Portal
Combined functions from functions_app.py and classes.py
Name: Hla Htoo
Semester: Spring 2023
Course : CS5001
"""

import functions_app
import classes
from typing import Union
import csv


def handle_load():
    """Handle the load command"""
    # get the name of the file that you want to load
    filename = functions_app.get_filename()
    try:
        # load the file
        record = classes.load_record_from_file(filename)
        print_list(record)
        return record
    except FileNotFoundError:
        functions_app.print_error(f'{filename} is not found! Please re-enter filename')


def print_list(record: classes.hospitalRecord):
    """
    prints the list of patients in the hospital record
    Args:
    record (hospitalRecord) : the record that you want to print
    returns: None
    """
    # prints the name of the record
    print(record)
    # loops through the patients in the record and print
    for i in range(0, record.size()):
        print(f'{i+1}. {record.patient_by_index(i)}')


def create_new_record():
    """
    creates a new hospital record (hospitalRecord)
    returns:
    the hospitalRecord that was created
    """
    # calls get_record_name() to get the name
    name = functions_app.get_record_name()
    print("New hospital record was created.")
    # create the hospitalRecord with the name and return 
    return classes.hospitalRecord(name)


def add_patient(record: classes.hospitalRecord):
    """
    adds patient to the record
    args:
    record (hospitalRecord) : the record that you want to add the patient to
    Returns: None
    """
    # call get_add_info() func to get the variables
    first_name, last_name, age, gender, dob = functions_app.get_add_info()
    person = classes.patient(first_name, last_name, age, gender, dob)
    # create the person object and add it to the record
    record.add_patient(person)
    print("------Patient added to the hopital record------")


def add_patient_visit(record: classes.hospitalRecord):
    """
    add visit summary to the patient object
    Args:
    record (hospitalRecord) : the record that the patient exists
    Returns: None
    """
    # calls the function and assign the correct patient to the variable
    person = functions_app.get_patient_info_for_visit(record)
    print("Patient found in record!")
    print(person)
    # calls get_add_visit_info() to get all the required info
    date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions = functions_app.get_add_visit_info()
    # add_visit_manually to add the visit to the person (create) object
    person.add_visit_manually(date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions)
    print("Visit summary was added successfully to the patient's record")


def view_patient_record(record: classes.hospitalRecord):
    """
    displays the info of the patient that you would like to view
    """
    person = functions_app.get_patient_info_for_visit(record)
    person.display_all_info()


def remove_patient(record: classes.hospitalRecord):
    """
    remove the patient from the record
    Args:
    record (hospitalRecord): the record which includes
    the patient that you want to remove
    """
    print("Please enter the name of the patient whose data you want to delete")
    # assign the right patient to the person variable
    person = functions_app.get_patient_info_for_visit(record)
    record.remove_patient(person)
    print("Patient's data has been deleted")


def save_file(record: classes.hospitalRecord):
    """
    Saves the data from record into csv files
    Args:
    record (hospitalRecord) : the record that you want to save
    """
    classes.save_record_to_file(record)


def create_new_account():
    """
    Creates a new admin account and stores it in account.csv file
    """
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
    # encrypt both username and password
    username = classes.encrypt(username)
    password = classes.encrypt(password)
    # create a dictionary with username and password
    account = {"username": username, "password": password}
    # open account.csv file and use Dictwriter to write the values to their respective fields
    with open('account.csv', 'a') as csv_file:
        csvwriter = csv.DictWriter(csv_file, fieldnames=['username', 'password'])
        csvwriter.writerow(account)


def main():
    """
    This is the main entry point fo2r the application.
    """
    # set the record vairable to none
    record = None
    # print welcome msg
    functions_app.print_welcome()
    # ask the user to log in and check if it matches the account and username
    access_granted = classes.login()  # use "hlahtoo" as username and "spring2023" as password
    # if access_granted is true
    if access_granted:
        # get the command
        command = functions_app.get_command_admin()
        # keep looping until the user wants to exit
        while command != functions_app.ViewOptionsAdmin.EXIT:
            # continue back to main function default to false unless the user changes account
            continue_to_main = False
            # if the user wants to load
            if command == functions_app.ViewOptionsAdmin.LOAD:
                record = handle_load()
            # if the ser wants to create a new record
            elif command == functions_app.ViewOptionsAdmin.CREATE:
                record = create_new_record()
            # if there is a record and the user wants to see the list from record
            elif record and command == functions_app.ViewOptionsAdmin.LIST:
                print_list(record)
            # if there is a record and the user wants to add more patients to the record
            elif record and command == functions_app.ViewOptionsAdmin.ADD:
                add_patient(record)
            # if there is a record and the user wants to add visit to the patient
            elif record and command == functions_app.ViewOptionsAdmin.ADDVISIT:
                add_patient_visit(record)
            # if there is a record and the user wants to remove the patient from the record
            elif record and command == functions_app.ViewOptionsAdmin.REMOVE:
                remove_patient(record)
            # if there is a record and the user wants to view one specific patient
            elif record and command == functions_app.ViewOptionsAdmin.VIEW:
                view_patient_record(record)
            # If the user wants to create a admin new account
            elif command == functions_app.ViewOptionsAdmin.NEWACCOUNT:
                create_new_account()
            # if the user wants to log out and login with another account
            elif command == functions_app.ViewOptionsAdmin.CHANGEACCOUNT:
                # then set the continue_to_true variable to True
                continue_to_main = True
            # if the user wants to save the record in csv files
            elif command == functions_app.ViewOptionsAdmin.SAVE:
                save_file(record)
            # if the record is not loaded or created and command is not unknown or exit then print warning msg
            elif record is None and command != functions_app.ViewOptionsAdmin.UNKNOWN and command != functions_app.ViewOptionsAdmin.EXIT:
                functions_app.print_error("Make sure to load or create the record data for a hospital")
            else:
                # if any unknown command was typed in, then print "Unknown command" and menu
                functions_app.print_error(f"Unknown command")
                functions_app.print_menu()
            # if continue_to_main is true, that means user wants to change the acc
            if continue_to_main:
                # call the main function again
                main()
                # set the command to exit so that it wont repeat again after recursion
                command = functions_app.ViewOptionsAdmin.EXIT
                # then return to stop the main
                return ...
            else:
                # unless the user type in exit, keep repeating the command
                command = functions_app.get_command_admin()
    # print good bye msg if the user is exiting the program
    functions_app.print_goodbye()
    # if record is not None, then save the file
    if record:
        save_file(record)
    return ...


if __name__ == "__main__":
    main()
