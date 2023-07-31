while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f'{index + 1}-{item.title()}'
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            index = number - 1
            new_todo = input("Enter new todo: ")

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos[index] = new_todo + "\n"

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            index = number - 1
            todos.pop(index)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print('Bye!')
