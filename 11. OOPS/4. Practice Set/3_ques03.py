# Create a class with a class attribute a; create an objct from it and set a direclty using object.a = 0. Does this change the class attribute ?
class Sample():
    a = "dhruv"

obj = Sample()
obj.a = "harry"
print(Sample.a)
print(obj.a)

# Ans: No