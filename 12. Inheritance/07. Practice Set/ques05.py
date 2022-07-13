class vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        finalStr = ""
        index = 0
        for i in self.vec:
            finalStr += f"{i}(a{index}) + "
            index += 1
        return finalStr[0:-2]

inputVector = vector([1, 4, 5, 6, 72, 3])
print(inputVector)