'''
Sets: collection of unique elements
sets is mutable but set element should be immutable like Number and string and tuple
not list or dictionary

- set is mutable
- set is unordered

'''

empty_set = set() # this is basically a constructor function that we are calling
print(empty_set)  # set()
print(type(empty_set))  # <class 'set'>

s = {1,2,3,4,5}
print(s)

s = {1,2,2,1,1,3}
print(s)
print(len(s))
print(s.copy())  # {1, 2, 3}


print(s)
s.add(100)
s.add(0)
print(s)
# s.clear()
# print(s) # set()

a = s.pop()
b = s.pop()
print(s)
print(a)
print(b)
print(s)
s.remove(100)
print(s)


'''
Set Methods:

1. s.add(val) : adds a value
2. s.remove(val) : removes a value
3. s.clear() : empties the set
4. s.pop() : removes a random value
5. s.union(set2) : returns a new union
6. s.intersection(set2) : returns new intersection

'''

s = {1,2,3,4,4,5,5}
print(s)
s.add(100)
s.add(200)
s.add(300)
print(s)  # {1, 2, 3, 4, 5, 100, 200, 300}

s.remove(3)
s.remove(5)
s.remove(200)
print(s)

x = s.pop()
y = s.pop()
# z = s.pop(4)
print(x)
print(y)
# print(z)  # TypeError: set.pop() takes no arguments (1 given)

s2 = {11,22,33, 4,4,44,100}
print(s)
print(s2)

set_union = s.union(s2)
print(set_union)

set_intersection = s.intersection(s2)
print(set_intersection)

# print(s.clear())  # None
# print(s)

s.clear()
print(s)  # set()
