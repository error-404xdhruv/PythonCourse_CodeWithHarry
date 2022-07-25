
'''
The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
'''

'''
Write a function to filter the vowels from a list
'''

def isVowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = letter.lower()
    if temp in vowels:
        return True
    else:
        return False


list1 = ['h', 'a', 'g', 't', 'e', 'r']
res = filter(isVowel, list1)
print(list(res))