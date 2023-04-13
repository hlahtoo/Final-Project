""" 
This is the main entry point for the application.
"""
import view, todo_list
from typing import Union


def handle_load(args: tuple) -> Union[todo_list.TodoList, None]:
    """Handle the load command"""
    if len(args) == 0:
        filename = view.get_filename()
    else:
        filename = args[0]
    try:
        todoList = todo_list.load_list_from_file(filename)
        view.print_list(todoList)
        return todoList
    except FileNotFoundError:
        view.print_error(f"File not found: {filename}")
        return None


def handle_save(todoList: todo_list.TodoList) -> None:
    """Handle the save command"""
    todo_list.save_list_to_file(todoList)


def handle_remove(todoList: todo_list.TodoList, args: tuple) -> None:
    """Handle the remove command"""
    if len(args) == 0:
        itemquery = view.get_item_query()
    else:
        itemquery = args[0]
    try:
        #index out of range error can occur
        item_index = int(itemquery) - 1
        item = todoList.get_item(item_index)
    except ValueError:
        item = todoList.find_item(itemquery)
    if item:
        todoList.remove_item(item)
    else:
        view.print_error(f"Item not found: {itemquery}")


def handle_complete(todoList: todo_list.TodoList, args: tuple) -> None:
    """Handle the complete command"""
    if len(args) == 0:
        itemquery = view.get_item_query()
    else:
        itemquery = args[0]
    try:
        #index out of range error can occur
        item_index = int(itemquery) - 1
        item = todoList.get_item(item_index)
    except ValueError:
        item = todoList.find_item(itemquery)
    if item:
        item.toggle_status()
    else:
        view.print_error(f"Item not found: {itemquery}")


def handle_add(todoList: todo_list.TodoList, args: tuple) -> None:
    """Handle the add command"""
    if len(args) == 0:
        shortName, description = view.get_add_info()
    else:
        shortName = args[0]
        if len(args) > 1:
            description = " ".join(args[1:])
        else:
            description = ""
    # will break if you put a comma in shortName
    todoList.add_item(todo_list.ListItem(shortName, description))


def handle_list(todoList: todo_list.TodoList) -> None:
    """Handle the list command"""
    view.print_list(todoList)


def handle_new(args: tuple) -> todo_list.TodoList:
    """Handle the new command"""
    if len(args) == 0:
        name = view.get_list_name()
    else:
        name = args[0]
    return todo_list.TodoList(name)


def main():
    """
    This is the main entry point fo2r the application.
    """
    todoList = None
    view.print_welcome()
    command, args = view.get_command()
    while command != view.ViewOptions.EXIT:
        if todoList and command == view.ViewOptions.LIST:
            handle_list(todoList)
        elif todoList and command == view.ViewOptions.ADD:
            handle_add(todoList, args)
        elif todoList and command == view.ViewOptions.REMOVE:
            handle_remove(todoList, args)
        elif todoList and command == view.ViewOptions.COMPLETE:
            handle_complete(todoList, args)
        elif todoList and command == view.ViewOptions.SAVE:
            handle_save(todoList)
        elif command == view.ViewOptions.LOAD:
            todoList = handle_load(args)
        elif command == view.ViewOptions.NEW:
            todoList = handle_new(args)
        elif todoList is None and command != view.ViewOptions.UNKNOWN and command != view.ViewOptions.EXIT:
            view.print_error("Make sure to load or create a new list first.")
        else:
            view.print_error(f"Unknown command: {' '.join(args)}")
            view.print_menu()
        command, args = view.get_command()
    if todoList:
        handle_save(todoList)
    view.print_goodbye()


if __name__ == "__main__":
    main()