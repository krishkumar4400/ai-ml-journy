# # File I/O - File input and output

# # operations: Read, Write, Append

# # File operations
# #   Open, read & close

# f = open("./26-test.txt", "r")  # return file object

# # data = f.read()

# # data = f.readline()

# # data = f.readlines()

# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)
# data = f.readline()
# print(data)


# print(data)
# print(type(data))  # <class 'str'>


# f = open("26-test.txt", 'w')
# f.write("This is new text\n the complete data")

# f.close()


# f = open('26-test.txt', 'a')

# f.write("\n\nNew text being appended to the file")
# f.close()

# f = open('26-sample.txt', 'x')

# f.write("New file created")

# f.close()


# r+, w+, a+
# f = open("26-sample.txt", "r+")
# f = open("26-sample.txt", "a+")
# f = open("26-sample.txt", "w+")

# f.write("123456")
# print(f.read())

# f.close()


# With keyword
with open("26-sample.txt", 'r') as f:
    # print(f.read())
    # print(f.read())
    # print(f.readline())
    data = f.read()
    print(type(data))
    print(len(data))
    print(data)