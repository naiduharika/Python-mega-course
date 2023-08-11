def get_todos(filename: str = "todos.txt") -> list[str]:
    """
    Read a text file and return the list of
    to-do items
    """
    with open(filename, 'r') as file:
        todos_list = file.readlines()
    return todos_list


def write_todos(todos_list: list, filename: str = "todos.txt") -> None:
    """
    Write the to-do items to a text file
    """
    with open(filename, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
