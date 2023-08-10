import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos_from_file(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button('Exit')

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event, values)

    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_to_file(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos_from_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_to_file(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todos_to_complete = values["todos"][0]
            todos = functions.get_todos_from_file()
            todos.remove(todos_to_complete)
            functions.write_to_file(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
