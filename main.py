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
    date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions =functions_app.get_add_visit_info()
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
    record = None
    functions_app.print_welcome()
    access_granted = classes.login()
    if access_granted:
        command = functions_app.get_command_admin()

        while command != functions_app.ViewOptionsAdmin.EXIT:
            continue_to_main = False
            if command == functions_app.ViewOptionsAdmin.LOAD:
                record = handle_load()
            elif command == functions_app.ViewOptionsAdmin.CREATE:
                record = create_new_record()
            elif record and command == functions_app.ViewOptionsAdmin.LIST:
                print_list(record)
            elif record and command == functions_app.ViewOptionsAdmin.ADD:
                add_patient(record)
            elif record and command == functions_app.ViewOptionsAdmin.ADDVISIT:
                add_patient_visit(record)
            elif record and command == functions_app.ViewOptionsAdmin.REMOVE:
                remove_patient(record)
            elif record and command == functions_app.ViewOptionsAdmin.VIEW:
                view_patient_record(record)
            elif command == functions_app.ViewOptionsAdmin.NEWACCOUNT:
                create_new_account()
            elif command == functions_app.ViewOptionsAdmin.CHANGEACCOUNT:
                continue_to_main = True
            elif command == functions_app.ViewOptionsAdmin.SAVE:
                save_file(record)
            elif record is None and command != functions_app.ViewOptionsAdmin.UNKNOWN and command != functions_app.ViewOptionsAdmin.EXIT:
                functions_app.print_error("Make sure to load or create the record data for a hospital")
            else:
                functions_app.print_error(f"Unknown command")
                functions_app.print_menu()
            if continue_to_main:
                main()
                command = functions_app.ViewOptionsAdmin.EXIT
                return ...
            else:
                command = functions_app.get_command_admin()
    functions_app.print_goodbye()
    if record:
        save_file(record)
    return ...


if __name__ == "__main__":
    main()
