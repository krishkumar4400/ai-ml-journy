def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(average(10,12,4))

# default values in function
# non-default first then default parameter
def fun(a=1,b=2):
    return a+b 

print(fun(5,6))