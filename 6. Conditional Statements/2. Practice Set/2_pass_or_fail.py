from unittest import result


print("Enter marks of 3 subjects: ")
list = []
result = "PASS"
total = int(0)
for i in range (0, 3):
    marks = int(input())
    total += marks
    list.append(marks)
    if (marks < 33):
        result = "PASS"

if(total <120):
    result = "FAIL"

print(result)