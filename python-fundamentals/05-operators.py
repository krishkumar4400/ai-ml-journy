'''
Arithmetic
Relational / Comparison
Assignment 
Logical
Bitwise
Membership
'''

# arithmetic operator
a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** 3)

# relational / comparison operator
a = 10
b = 20

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)
print(a == b)


# assignment operator

'''
=
+=
-= 
*=
/=
**=
%=
'''

a = 10
b = 20

#  =
print(a)
a = 200
print(a)

a = a+1
print(a)

a += 1
print(a)

a -= 100
print(a)


# Logical operator
'''
and
or
not : it reverse the value : true -> false  false -> true
'''

var = True
print(not var) # false

print(not(5 > 8))

a = 10
b = 20

print(not a) #False

print((a > b) and (b > a))

print((a > b) or (b > a))

print((1 > 2) or (2 > 2))

