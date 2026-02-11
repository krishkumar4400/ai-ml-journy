# lamda functions are small anonymous functions defined by lambda keyword
'''
Lambda functions are not used to perform complex operations 
it is generally used for small tasks and computations and small mathematical operations

it can have multiple parameters but only single expression

after doing operation it automatically return the value

Uses of lambda functions:
    - it is used in higher order functions
    (higher order functions are those who takes function as parameter or return a function from itself)
    eg: def fun(function):
            _________
            _________
            _________
'''

sum = lambda a,b,c : a+b+c
print(sum(1,2,3)) #6

sub = lambda a,b : a-b
print(sub(10,5)) #5

multiply = lambda a,b,c : a*b*c
print(multiply(2,5,10)) #100

division = lambda a,b : a/b
print(division(50,2)) #25

