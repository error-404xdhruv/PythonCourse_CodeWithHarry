
# python has a rule that initialising index is inclusive but terminating index is exclusive

s = "Indian"

print("Length: ", len(s))

# printing a string s from 0th index to index i-1 use print(s[:i])
print(s[:4])

# printing a string s from index a to index b use print(s[a:b+1]) 
print(s[2:6])

# printing a string s from index a to end
print(s[4:])

# printing using -ve index
print(s[-4:-1])