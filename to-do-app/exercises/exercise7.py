filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(f'../files/{filename}', 'r')
    lines = file.read()
    file.close()
    print(lines)
