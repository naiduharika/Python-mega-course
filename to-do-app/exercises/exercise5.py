user_input = input("Add a new member: ")

file = open('../files/members.txt', 'r')
members = file.readlines()
file.close()

members.append(user_input.title() + "\n")

file = open('../files/members.txt', 'w')
file.writelines(members)
file.close()
