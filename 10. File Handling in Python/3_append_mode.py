
# append mode can be considered as a sub function of write mode, in append mode all the things which you do is written at the end of the file selected, but in write mode it would clear all the data of the file and then rewrite the whole file from start

file = open('sample.txt', 'a')
file.write('\nThis will add new line at the end, everytime this program is runned.')
file.close()

file = open('sample.txt', 'r')
print(file.read())
file.close()