from decimal import ROUND_FLOOR
import math

a = 3.451678

# trunc function - removes all the digits after decimal and returns pure integer value
print(math.trunc(a))

# ceil function - returns intger greater than or equal to the given number
print(math.ceil(a))

# floor function - returns integer smaller than or equal to the given number
print(math.floor(a))

# precision handling
# lets assume we have to only print the decimal number upto 2 decimal places only
print(round(a, 2))
# there are other ways to to this also but its the most efficient one