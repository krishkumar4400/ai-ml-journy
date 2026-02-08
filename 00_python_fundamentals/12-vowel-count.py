vowels = ['a', 'e', 'i', 'o', 'u']
words = input("Enter a word: ")
count=0

for word in words:
    if(word.lower() in vowels):
        count+=1

print(count)