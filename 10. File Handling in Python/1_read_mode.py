""" Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.  """

# opening a file in read mode 
file = open('sample.txt', 'r')

# printing each line in the file one by one , method 1
""" for line in file:
    print(line) """

# printing each line in the file one by one, method 2
""" print(file.read()) """

# printing first n number of characters in the file, (method 3)
print(file.read(5))

# it is very important to close the file after the work gets completed
file.close()