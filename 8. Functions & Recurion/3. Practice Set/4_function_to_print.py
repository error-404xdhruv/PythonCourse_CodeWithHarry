def printPattern (n):
    if (n == 0):
        return
    print("* " * n)
    printPattern(n-1)

n = int(input())
printPattern(n)