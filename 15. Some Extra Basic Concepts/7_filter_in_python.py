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

list1  = ['h', 'a', 'g', 't', 'e', 'r']
res = filter(isVowel, list1)
print(list(res))