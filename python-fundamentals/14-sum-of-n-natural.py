# print sum of 'n' natural numbers

num = int(input("Enter a natural number: "))

sum = 0

for i in range(1, num+1):
    sum += i

print(sum)

# formula:
print((num * (num + 1)) / 2 ) # float