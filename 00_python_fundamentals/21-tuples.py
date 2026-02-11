'''
Tuples: Immutable sequence of values


'''

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

tup = (1,2,3,4,5,6)
print(tup)
print(type(tup))

t1 = (1,2,3,3.14,'A', "xyz", "krish", 889.11)
print(t1)
print(t1[0])
print(t1[3])

# t1[3] = 10  # TypeError: 'tuple' object does not support item assignment

# single valued list and tuple:
l = [10]
print(l)
print(type(l))

t = (100) # expression
print(t) # 100
print(type(t))  # <class 'int'>
t = (100,)
print(t)  # (100,)
print(type(t))  # <class 'tuple'>
t = ("abc")
print(t)  # abc
print(type(t))  # <class 'str'>


# slicing in tuple
print(tup)
print(tup[:])

# loops with tuple
tup = (1,2,3,4,5,6,7,8,9,10)
print(tup)

sum = 0
for val in tup:
    # print(val)
    sum += val
    
print(sum)


'''
Tuple Methods:
1. t.index(val) : returns 1st occurrence idx
2. t.count(val) : counts total occurences
'''

t2 = (1,1,2,3,2,4,4)
print(t2.index(3)) # 3
print(t2.count(1)) # 2
