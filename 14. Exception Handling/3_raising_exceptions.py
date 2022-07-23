def increment(a):
    try:
        return int(a) + 1
    except:
        raise ValueError("This is not good.")


a = increment('a')
print(a)

# we can raise custom exceptions using the raise keyword in Python