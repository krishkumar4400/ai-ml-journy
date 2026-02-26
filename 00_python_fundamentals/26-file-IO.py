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
# with open("26-sample.txt", 'r') as f:
#     # print(f.read())
#     # print(f.read())
#     # print(f.readline())
#     data = f.read()
#     print(type(data))
#     print(len(data))
#     print(data)

# with open("26-sample.txt") as f:
#     data = f.readlines()
#     print(data)
#     print(type(data))
#     print(len(data))


# # delete files
# import os
# os.remove('./26-sample.txt')


# # Practice Problem
# with open('26-sample.txt', 'r') as f:
#     data = f.read()
#     lst = data.split(' ')
#     idx = 0
#     print(lst)
#     for val in lst:
#         if val == 'Python':
#             print(val)
#             print(idx)
#         idx+=1

# Practice Problem
with open("26-sample.txt", "r") as f:
    data = f.readlines()
    line=0
    for val in data:
        lst = val.split(" ")
        for word in lst:
            if(word == "Python"):
                print(word)
                print(line)
        line+=1