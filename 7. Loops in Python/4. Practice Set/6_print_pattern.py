n = int(input())
for i in range (0, n):
    print("  " * (n-i-1), end = '')
    print("* " * (i*2+1))