contents = ["All carrots are to be sliced longitudinally.",
            "the carrots were reportedly sliced.",
            "the slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)
