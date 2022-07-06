# Search for the word 'Python' in a log file.

""" with open ("log_file.txt", "r") as file:
    content = file.read()

if ('Python' in content):
    print("YES")
else:
    print("NO") """

# The most standard way to open the file if you have to search a word is to open it in lower case, eg-
with open ("log_file.txt", "r") as file:
    content = file.read()

if ('python' in content.lower()):
    print("YES")
else:
    print("NO")