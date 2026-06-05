<<<<<<< HEAD
try:
    with open('sample.txt') as file:
        content = file.read()

    #content_capitalized = content.upper()
    print("File content: ")
    #print(content_capitalized)
    print(content)
    print("Done")
except FileNotFoundError:
    print("File not found.")
=======
user_input = input("Enter some text: ")

with open('sample.txt') as file:
    content = file.read()
    
    
with open("user_file.txt", "w") as file:
    file.write("user_input: " + user_input)
    
    
#content_capitalized = content.upper()
print("File content: ")
#print(content_capitalized)
print(content)
print("Done")
>>>>>>> feature/write-capability
