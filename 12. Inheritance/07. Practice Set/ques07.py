from turtle import begin_fill

# Print the dimension of the vector
class vector:
    def __init__ (self, vec):
        self.vec = vec
    def dim (self):
        return len(self.vec)
    
    # this woudl also do the same thing
    def __len__ (self):
        return len(self.vec)

vector1 = vector([5, 3, 1, 4])

# method 1
print(vector1.dim())

# method 2
print(len(vector1))