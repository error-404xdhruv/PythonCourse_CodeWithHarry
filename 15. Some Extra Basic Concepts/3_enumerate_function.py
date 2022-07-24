# Enumerate Function adds a counter variable to an iterable and returns it
sampleList = [12, 4.5, "dhruv"]

'''
# now suppose the following code
index = 0
for i in sampleList:
    print(f"{index}\t{i}")
    index+=1
'''
# we can do the same work using enumerate function
for index, i in enumerate(sampleList):
    print(f"{index}\t{i}")