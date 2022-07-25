'''
Write a function to filter the vowels from a list
'''

def isVowel (letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = letter.lower()
    if letter in vowels:
        return True
    else:
        return False

list  = ['h', 'a', 'g', 't', 'e', 'r']
filteredList = filter(isVowel, list)
for i in filteredList:
    print(i)

print(filteredList)