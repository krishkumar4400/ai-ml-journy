# # loops

# # 1. while loop
# x = 1 #iterator

# while(x <= 10):
#     print(x)
#     x = x + 1

# # multiplication table of number n
# n = int(input("Enter a number: "))

# i = 1
# while(i <= 10):
#     print(f"{n} X {i} = {n * i}")
#     i += 1


#  break and continue
# i = 1
# while(i < 100):
#     if(i % 5 == 0):
#         break
#     print(i)
#     i += 1
# print("Outside loop now")

# j = 0
# while(j < 10):
#     j += 1
#     if(j % 3 == 0):
#         continue
#     print(j)
    
# print all the odd numbers from 1 to 10
# num = 0
# while(num <= 10):
#     if(num % 2 == 0):
#         num += 1
#         continue
#     print(num)
#     num += 1
    
# num2 = 11
# while(num2 <= 20):
#     if(num2 % 2 != 0):
#         print(num2)
#     num2 += 1
    
# num3 = 21
# while(num3 <= 30):
#     print(num3)
#     num3 += 2
    

# string  = "Hello"


# #  for loop: used for sequential traversal - sequence like: list, tuple, dictionary, sequence, string

# for var in string:
#     print(var)
    
# # in => membership operator - used to check presence

# if "o" in string:
#     print("O Exists In String.")
    

# for i in range(10): #max value - 0 to 9 (0 to n-1)
#     print(i)


# count i in the phrase
phrase = "Artificial Intelligence"
count = 0
for char in phrase:
    if(char.lower() == 'i'):
        count=+1
    
print("count = ", count)



