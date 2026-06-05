with open('sample.txt') as file:
    content = file.read()

content_capitalized = content.upper()
print("File content: ")
print(content_capitalized)
print("Done")