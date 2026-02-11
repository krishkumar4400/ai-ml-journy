"""
Strings - we can create strings using single, double or tripple quotes

generally
for word we use double quotes = ""
word = "python

and for single character we use single quote - ''
char = 'A'


**** String - String is basically a sequence of characters. It stores sequence of characters.

In python strings are immutable means we can change, reassign or update its index value

"""

word = "Python"

print(len(word))

# concatenate
word1 = "I Love"
line = word1 + " " + word
print(line)

# Indexing - access position
print(word)
print(word[0])
print(word[1])
print(word[0:])  # python
print(word[0:4])  # pytho
print(word[2:4])  # th

# traversing the string
print("Traverse String")
for i in range(len(word)):
    print(word[i])

# or
for ch in word:
    print(ch)


"""
String operations
1. slicing
"""

"""
slicing - extracting the substring 

str = "Python"
str[st:idx, end:idx], end not included
"""
string = "Python"
print(string[2:4])

sentence = "I study from Apnacollege"
print(sentence[13:24])
print(sentence[13:])
print(sentence[13 : len(sentence)])
print(sentence[:])
# negative
print(sentence[5:2:-1])  # dut
print(sentence[-1:-5:-1])  # egel
print(sentence[-1::-1])  # egellocanpA morf yduts I
print(sentence[-5::])
print(sentence[-5:-1])


"""
String Formatting - creating dynamic string (dynamic string means string having text, values, variables, expressions)

2 ways to create dynamic strings or formatting
    1. format() function - it uses placeholder {} and placement values
    2. f-strings


"""

a = 5
b = 10
sum = a + b

print("The sum is {}".format(sum))  # The sum is 15
print("The language is {}".format("Python"))  # The language is Python
print("The sum of {} and {} is {}".format(a, b, sum))  # The sum of 5 and 10 is 15

# index based formatting
print("The sum of {1} & {0} is {2}".format(a,b,sum))

# value based formatting
print("values of vars {a} & {b}".format(a=100, b=200))
print("values of vars {b} & {a}".format(a=100, b=200))

# we can also reuse the values
print("{a}values {a} of vars {b} & {a} {a} - {b}".format(a=100, b=200))


# Formatting using F-Strings - we use 'Literal string interpolation in f strings means we can embed expressions in the string itself'
print(f"The sum of {10} and {20} will be {10+20} and the subtraction will be {20-10}")


