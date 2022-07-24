"""
Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files does not exist, a message without exiting the program must be printed prompting the same.
"""
def openfile (filename):
    try:
        with open (filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{filename} not found.")

while(True):
    command = input("Enter 'Q' to exit or Enter the file name to search for the content: ")
    if (command == 'Q'):
        break ;
    else:
        openfile(command)