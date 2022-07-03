
# write mode 
# if you select a file which does not exist the write mode would create a file with name in the same directory (but in read mode it would give error if you tried opening a file which does not exist or even when you provide the path to wrong directory)

file = open('sampleWriteMode.txt', 'w')
file.write("sample_command")
file.close()

file = open('sampleWriteMode.txt', 'r')
print(file.read())
file.close()