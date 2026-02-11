# WAF to print factorial of 'n'
'''
n! = 1*2*3* ..... * n

5! = 1*2*3*4*5 = 120 -> 1 to n -> 1 to 5
'''

def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

n = int(input("Enter N: "))
print(factorial(n))