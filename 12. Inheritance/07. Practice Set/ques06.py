
# Write __str__() method to print the vector as follows: 7i + 8j + 10

class vector:
    def __init__(self, vec):
        self.vec = vec
    
    def __str__ (self):
        return f"{self.vec[0]}i  + {self.vec[1]}j + {self.vec[2]}k"

sample = vector([2, 4, 5])
print(sample)