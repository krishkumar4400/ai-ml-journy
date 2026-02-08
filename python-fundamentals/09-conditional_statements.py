age = int(input("Enter age: "))

if(age < 13):
    print("child")
elif(age >= 13 and age <= 18):
    print("teenager")
else:
    print("adult")
    

# Nesting:
username = input("Enter username: ")
password = input("Enter password: ")
if(username == "user"):
    if(password == "pass"):
        print("login successfull")
    else:
        print("password is incorrect")
else:
    print("username is incorrect")
        
        
if(username == "user" and password == "pass"):
    print("login successfull")
else:
    if(username != "user"):
        print("username is incorrect")
    else:
        print("wrong password")
        