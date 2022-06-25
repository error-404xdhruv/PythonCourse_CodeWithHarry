
s = "Lorem ipsum ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation"

# len function: counts the length of the whole string
print(len(s))

# endswith function: its a boolean function which return true if the string ends with the specific keyword else false
print(s.endswith("tion"))
print(s.endswith("dhruv"))

# count function : counts the total occurences of any character or sub-string in the whole string
print(s.count('l'))
print(s.count("ipsum"))

# capitalise : to_upper but to just the first character of the string
print(s.capitalize())

# find function : finds the first occurences of the specified word or character
print(s.find('L'))
print(s.find("ipsum"))

# replace function : replaces the old word with new word in the whole string -->
# print(s.replace("old word", "new word"))

print(s.replace("ipsum", "hey"))