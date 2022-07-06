# write a program to rename an existing file using Python

# Method 1: We can copy the data of the file which is to be deleted to a variable content and then write content to some other file which is named after the new name and then delete the prev file
# Code for Method 1:
import os

with open ("file_to_be_deleted.txt", "r") as file:
    content = file.read()

with open ("file_to_be_copied.txt", "w") as file:
    file.write(content)

os.remove("file_to_be_deleted.txt")