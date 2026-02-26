# some errors in program are known and can be predicted called exception
# and to handle and manage or taking action accordingly on an excaption called exception handling
# In exception we basically try to predict wha are the possible errors that can occur in our program and we try to manage them try to handle these errors.

# The code that might cause an error and can block or disrrupt the execution of code written in try block.


# try:
#     x = int(input("Enter a number: "))
#     ans = 10/x
#     print(ans)
# except Exception as e:
#     # print("The number can't be divided by ZERO")
#     # print(e.add_note("string"))
#     # print(e.args)  # ('division by zero',)
#     # print(e.with_traceback(None))  # division by zero
#     print(e)  # division by zero


try:
    x=int(input("Enter x: "))
    ans = 10/x
    
except ZeroDivisionError:
    print("Divide by 0 is not allowed")
except TypeError:
    print("")
    
except ValueError:
    print("Invalid input")
else:
    print(ans)
    
finally:
    print("END of python program")
    
# Built in exceptions link -> w3schools
