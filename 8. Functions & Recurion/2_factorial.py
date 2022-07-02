def factorial_revursive (n):
    if (n == 0 or n ==1):
        return 1
    else:
        return n * factorial_iterative(n-1)

def factorial_iterative (n):
    ans =1
    for i in range (1, n+1):
        ans = ans * i
    return ans

n = int(input())
print(factorial_iterative(n))
print(factorial_revursive(n))