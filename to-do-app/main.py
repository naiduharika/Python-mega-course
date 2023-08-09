# from functions import get_todos_from_file, write_to_file
import functions
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # Get user input and strip space char from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos_from_file()

        todos.append(todo)

        functions.write_to_file(todos)
        print(f"Todo {todo.title().strip()} was added to the list")
    elif user_action.startswith('show'):
        todos = functions.get_todos_from_file()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item.title()}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos_from_file()

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            functions.write_to_file(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos_from_file()
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_to_file(todos)
            message = f"Todo {todo_to_remove.title()} was removed from the list"
            print(message)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Bye!')
