
# a file contains a word "Donkey" multiple times. You need to write a program which replaces this word with !@#$%^ by updating the same file.

with open("sample4.txt", "r") as file:
    content = file.read()

# what we did ?- first we stored / read the content of the file in the variable content and then we would replace all the words donkey with !@#$%^
content = content.replace("donkey", "!@#$%^")

with open("sample4.txt", "w") as file:
    file.write(content)