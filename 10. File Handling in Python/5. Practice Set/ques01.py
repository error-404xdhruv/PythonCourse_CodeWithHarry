
# write a program to read the text from a given file and find out whether it contains the word 'twinkle'

with open('ques01_poem.txt', 'r') as file:
    data = file.read()
    if ('twinkle' in data):
        print("Yes")
    else:
        print("No")