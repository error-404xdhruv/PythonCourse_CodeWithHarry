
# what it does:- we took i = 1 initially and in while loop means "jb tk i <= 10 tb tk keep going and inside loop we keep incrementing i by 1 with each iteration"

i = 1
while (i <= 10):
    print("i =", i)
    i += 1

# for loop:- start with x = 0 and go till x = 9 because in range (0, 10) 10 is exlusive in python and thats the rule

for x in range(0, 10):
    print("Goto Hell!")

# print items of a List using Loops
name = ["dhruv", "abh1shank", "divyam", "aviral"]
i = 0
while (i < len(name)):
    print(name[i])
    i += 1

print("\nUsing For Loop")
# print items of a list using for-loop
for i in name :
    print(i)

# for loop
for i in range (1, 11):
    print(i)

print("--------------------")

# for loop with step size
for i in range (1, 11, 2):
    print(i)