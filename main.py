
try:
    with open('sample.txt') as file:
        content = file.read()

    #content_capitalized = content.upper()
    print("Welcome to the File Manager Application!")
    print("File content: ")
    #print(content_capitalized)
    print(content)
    print("Done")


    user_input = input("Enter some text: ")

        
        
    with open("user_file.txt", "w") as file:
        file.write("user_input: " + user_input)
    


except FileNotFoundError:
    print("File not found.")