# Type Conversion -> convert the type of data from one to another
    # type conversion can be done with only compatible type data
    # eg: int -> float
    # float -> int
    # int -> bool
    
    # "abc123" -> int (not possible)
    
    
'''
float + int = float

conversion - type conversion, type casting

type conversion -> (implicit -> python does automatically)
type casting -> (explicit -> do programmer)
'''

print(type(10/2)) # <class 'float'>

ans = 10 + 20.8
print(type(ans)) # <class 'float'>


# Explicit - Casting
ans1 = 10 + 10.5 #conversion
ans2 = int(10 + 10.5) #casting

print(ans1, type(ans1))
print(ans2, type(ans2))

print("123", type("123"))
print(int("123"), type(int("123")))


# bool -> zero value - false, non zero value - true
val = bool(0)
print(val, type(val))

val = bool(10)
print(val, type(val))

val = bool(-2)
print(val, type(val))

# False <class 'bool'>
# True <class 'bool'>
# True <class 'bool'>