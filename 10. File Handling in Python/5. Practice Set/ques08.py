# write a program to check whether two file are identical or not
with open ("match1.txt", "r") as file:
    content1 = file.read().lower()
with open ("match2.txt", "r") as file:
    content2 = file.read().lower()

if (content1 == content2):
    print("Yes, they are identical.")
else:
    print("No")