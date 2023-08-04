def get_todos_from_file(filename):
    with open(filename, 'r') as file:
        todos_list = file.readlines()
    return todos_list


def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)


while True:
    # Get user input and strip space char from it
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = get_todos_from_file('files/todos.txt')

        todos.append(todo)

        write_to_file('files/todos.txt', todos)
        print(f"Todo {todo.title().strip()} was added to the list")
    elif user_action.startswith('show'):
        todos = get_todos_from_file('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item.title()}'
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = get_todos_from_file('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            write_to_file('files/todos.txt', todos)
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

            todos = get_todos_from_file('files/todos.txt')
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_to_file('files/todos.txt', todos)
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
