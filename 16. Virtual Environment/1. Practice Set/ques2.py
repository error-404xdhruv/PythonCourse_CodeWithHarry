'''
Write a program to filter a list of numbers which are divisible by 5
'''


def isDiv(n):
    if (n % 5 == 0):
        return True
    else:
        return False


list1 = [2, 3, 4, 5, 10, 15, 12, 11]
res = filter(isDiv, list1)
print(list(res))