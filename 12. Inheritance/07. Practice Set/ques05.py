
# Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot product of them.

class vector:
    def __init__(self, vec):
        self.vec = vec

    def __add__(self, vec2):
        sumVector = []
        for i in range(len(self.vec)):
            sumVector.append(self.vec[i]+vec2.vec[i])
        return vector(sumVector)
    
    def __mul__ (self, vec2):
        sum = 0
        for i in range (len(vec2.vec)):
            sum += self.vec[i]*vec2.vec[i]
        return sum

    def __str__(self):
        finalStr = ""
        index = 0
        for i in self.vec:
            finalStr += f"{i}(a{index}) + "
            index += 1
        return finalStr[0:-2]


inputVector = vector([1, 2, 3])
inputVector2 = vector([3, 4, 5])
print(inputVector + inputVector2)
print(inputVector*inputVector2)