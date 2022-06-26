
minidic = {
    'naam' : 'name' ,
    'bharat' : 'india',
    'khatarnak' : 'dangerous'
}

print(f"Enter the word you want to search meaning of --> Options are: {minidic.keys()}")

word = input()
print(f"Ans: {minidic[word]}")