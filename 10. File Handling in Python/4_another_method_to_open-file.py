
# with this method we dont need to close the file separately

with open('sample.txt', 'r') as file:
    print(file.read())

with open('sample.txt', 'w') as file:
    file.write('hello world')

with open('sample.txt', 'r') as file:
    print(file.read())