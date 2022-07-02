# write a python function to remove a given word from a string and strip it at the same time

# let see what is strip the string
str = "              Hello , World    hello boi     "
print(str)
# it removes extra spaces from the start and from the end of the string
print(str.strip())

# creating function
def remove_and_strip(string, word):
    string = string.replace(word, "")
    return string.strip()

print(remove_and_strip(str, 'boi'))