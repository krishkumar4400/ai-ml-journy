"""
Lists:
    mutable sequence of values

"""

marks = [100, 99, 89, 88, 90]
print(marks)
print(len(marks))

for value in marks:
    print(value)

print(marks[0])
print(marks[1])
# print(marks[11])  # IndexError: list index out of range

marks[0] = 111
print(marks)

lst = [100, 30, 55, "abc", "X", 100.99]
print(lst)
print(type(lst))

# list slicing
print(lst[:3])
print(lst[3:])
print(lst[: len(lst)])
print(lst[4 : len(lst)])
print(lst[4:])
print(lst[-4:])
print(lst[-4:-1])

"""
slicing creates:
string -> substring
list -> sublist

str[st idx:end idx]
list [st idx:end idx]

"""

"""
List methods -> methods:
1. l.append(val) : add one element at the end
2. l.insert(index,val) : insert element at index
3. l.sort() : arranges in increasing order
4. l.reverse() : reverses order
5. l.pop() : delete last element and return  # index (default last).

list -> classes -> functions -> methods 
"""

l = []
print(l)
l.append("krish")
l.append("ankit")
print(l)
a = l.pop()
print(l)
print(a)
l.pop(0)
print(l)

l2 = [1, 2, 3, 4]
print(l2)

l2.insert(1, 20)
print(l2)
l2.extend([5, 5, 5, 5])
l2.extend((4, 4, 4, 4))
print(l2)  # [1, 20, 2, 3, 4, 5, 5, 5, 5, 4, 4, 4, 4]

l2.reverse()
print(l2)

l2.sort()
print(l2)

l2.sort(reverse=True)
print(l2)


# Loops with lists
nums = [1, 2, 3, 4, 5, 6]
for val in nums:
    print(val)


# linear search
x = 5
idx = 0
for val in nums:
    if val == x:
        print(f"Index = {idx}")
        break
    idx += 1
