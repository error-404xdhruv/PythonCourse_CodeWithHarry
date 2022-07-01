from gettext import find


nameList = ["shivyam", "shivaay", "dhruv", "sohan", "lol"]
for name in nameList:
    if (name.startswith('S') or name.startswith('s')):
        print("Welcome,", name)