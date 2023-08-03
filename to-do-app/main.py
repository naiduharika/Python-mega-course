def read_file(filename):
    with open('files/todos.txt', 'r') as file:
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
    if 'add' in user_action:
        todo = user_action[4:] + "\n"

        todos = read_file('files/todos.txt')

        todos.append(todo)

        write_to_file('files/todos.txt', todos)
        print(f"Todo {todo.title().strip()} was added to the list")
    elif 'show' in user_action:
        todos = read_file('files/todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1}-{item.title()}'
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        index = number - 1

        todos = read_file('files/todos.txt')

        new_todo = input("Enter new todo: ")
        todos[index] = new_todo + "\n"

        write_to_file('files/todos.txt', todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])
        index = number - 1

        todos = read_file('files/todos.txt')
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        write_to_file('files/todos.txt', todos)
        message = f"Todo {todo_to_remove.title()} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")

print('Bye!')
