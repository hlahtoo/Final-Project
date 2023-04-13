import functions_app
import classes
from typing import Union

def handle_load(args: tuple) -> Union[classes.hospitalRecord, None]:
    """Handle the load command"""
    if len(args) == 0:
        filename = functions_app.get_filename()
    else:
        filename = args[0]
    try:
        todoList = classes.load_list_from_file(filename)
        functions_app.print_list(todoList)
        return todoList
    except FileNotFoundError:
        functions_app.print_error(f"File not found: {filename}")
        return None
    
def main():
    """
    This is the main entry point fo2r the application.
    """
    todoList = None
    functions_app.print_welcome()
    command, args = functions_app.get_command()
    while command != functions_app.ViewOptions.EXIT:
        if todoList and command == functions_app.ViewOptions.LIST:
            handle_list(todoList)
        elif todoList and command == functions_app.ViewOptions.ADD:
            handle_add(todoList, args)
        elif todoList and command == functions_app.ViewOptions.REMOVE:
            handle_remove(todoList, args)
        elif todoList and command == functions_app.ViewOptions.COMPLETE:
            handle_complete(todoList, args)
        elif todoList and command == functions_app.ViewOptions.SAVE:
            handle_save(todoList)
        elif command == functions_app.ViewOptions.LOAD:
            todoList = handle_load(args)
        elif command == functions_app.ViewOptions.NEW:
            todoList = handle_new(args)
        elif todoList is None and command != functions_app.ViewOptions.UNKNOWN and command != functions_app.ViewOptions.EXIT:
            functions_app.print_error("Make sure to load or create a new list first.")
        else:
            functions_app.print_error(f"Unknown command: {' '.join(args)}")
            functions_app.print_menu()
        command, args = functions_app.get_command()
    if todoList:
        handle_save(todoList)
    functions_app.print_goodbye()


if __name__ == "__main__":
    main()