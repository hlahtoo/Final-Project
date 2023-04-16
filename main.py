import functions_app
import classes
from typing import Union
import csv

def handle_load():
    """Handle the load command"""
    
    filename = functions_app.get_filename()
    try:
        record = classes.load_record_from_file(filename)
        print_list(record)
        return record
    except FileNotFoundError:
        functions_app.print_error(f'{filename} is not found! Please re-enter filename')

def print_list(record):
    print(record)
    for i in range(0, record.size()):
        print(f'{i+1}. {record.patient_by_index(i)}')

def create_new_record():
    name = functions_app.get_list_name()
    print("New hospital record was created.")
    return classes.hospitalRecord(name)

def add_patient(record: classes.hospitalRecord):
    first_name, last_name, age, gender, dob = functions_app.get_add_info()
    person = classes.patient(first_name, last_name, age, gender, dob)
    record.add_patient(person)
    print("------Patient added to the hopital record------")

def add_patient_visit(record: classes.hospitalRecord):
    person = functions_app.get_patient_info_for_visit(record)
    print(person)
    date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions =functions_app.get_add_visit_info()
    person.add_visit_manually(date, blood_pressure, temp, pulse, oxy_saturation, symptoms, doctor, instructions)
    print("Visit summary wasadded successfully to the patient's record")

def view_patient_record(record: classes.hospitalRecord):
    person = functions_app.get_patient_info_for_visit(record)
    person.display_all_info()

def remove_patient(record: classes.hospitalRecord):
    """
    remove the patient from the record
    """
    print("Please enter the name of the patient whose data you want to delete")
    person = functions_app.get_patient_info_for_visit(record)
    record.remove_patient(person)
    print("Patient's data has been deleted")

def save_file(record: classes.hospitalRecord):
    classes.save_record_to_file(record)
    
def create_new_account():
    username = input("Enter username: ").strip()
    password = input("Enter password: ")
    account = {"username": username, "password": password}
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
                pass
            elif record is None and command != functions_app.ViewOptionsAdmin.UNKNOWN and command != functions_app.ViewOptionsAdmin.EXIT:
                functions_app.print_error("Make sure to load or create the record data for a hospital")
            else:
                functions_app.print_error(f"Unknown command")
                functions_app.print_menu()
            command = functions_app.get_command_admin()
    functions_app.print_goodbye()
        
    if record:
        save_file(record)
        


if __name__ == "__main__":
    main()