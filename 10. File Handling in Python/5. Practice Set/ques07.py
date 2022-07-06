
# write a program to make a copy of text file
with open("copy.txt", 'r') as file:
    content = file.read()

with open("paste.txt", "w") as file:
    file.write(content)