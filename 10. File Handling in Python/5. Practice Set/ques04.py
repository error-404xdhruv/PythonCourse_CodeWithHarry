
# repeat the ques03 for a list of such words to be censored.

# lets create a word which needs to be replaced
badWords = ["donkey", "saale", "motu", "haathi"]

with open ("sample4.txt", "r") as file:
    content = file.read()

for word in badWords:
    content = content.replace(word, "!@#$%^")

with open ("sample4.txt", "w") as file:
    file.write(content)

"""
donkey saale motu etc etc etc
donkey saale motu etc etc etc
donkey saale motu etc etc etc
donkey saale motu etc etc etc
donkey saale motu etc etc etc
donkey saale motu etc etc etc
donkey saale motu etc etc etc
"""