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

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            todos = read_file('files/todos.txt')

            todos.append(todo)

            write_to_file('files/todos.txt', todos)
        case 'show' | 'display':
            todos = read_file('files/todos.txt')
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{index + 1}-{item.title()}'
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            index = number - 1

            todos = read_file('files/todos.txt')

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + "\n"

            write_to_file('files/todos.txt', todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            index = number - 1

            todos = read_file('files/todos.txt')
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_to_file('files/todos.txt', todos)
            message = f"Todo {todo_to_remove.title()} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print('Bye!')
