# File I/O - File input and output

# operations: Read, Write, Append

# File operations
#   Open, read & close

f = open("./26-test.txt", "r") # return file object

data = f.read()

print(data)
print(type(data))  # <class 'str'>

f.close()
