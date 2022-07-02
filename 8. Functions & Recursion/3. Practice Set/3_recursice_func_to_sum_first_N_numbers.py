def findSum (n, i, sum):
    if (i==n+1):
        print(sum)
        return
    sum += i
    findSum(n, i+1, sum)

n = int(input())
findSum(n, 1, 0)