a = 10
def change():
    global a
    # notice the difference b/w the output by commenting the just above line
    a += 5
    print(f"Value of a inside Function: {a}")

change()
print(f"Value of a outside function: {a}")