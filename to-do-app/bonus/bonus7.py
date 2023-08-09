filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [f"{filename.replace('.', '-')}.txt" for filename in filenames]

print(filenames)