# Lambda Functions are anonymous functions means that the function is without a name.
# Format:
# functions_name = lambda arguement1, arg2, .... : function

# Let say we have to create a function which adds three numbers
# method 1
def sum (x, y, z):
    return x  + y + z

# method 2
sum_using_lambda = lambda x, y, z: x+y+z

print(sum(1, 2, 3))
print(sum_using_lambda(1, 2, 3))

multiply_custom = lambda x, y : x*y
print(multiply_custom(2, 3))