import re

def register():
    with open('user_detail.txt', 'a')as user_file:
        username = []
        password =[]
        data = open('user_detail.txt', 'r')
        for i in data:
            u, p = i.split(",")
            u = u.strip()
            username.append(u)
            password.append(p)
        email = input('Enter Email : ')
        emailPattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        password = input('Enter Password: ')
        passwordPattern = re.compile(r'[a-zA-Z0-9@#!$%^&*]{8,}')
        if email in username:
            print("User already Exsist")
        elif email == emailPattern.fullmatch(email):
            if password == passwordPattern.fullmatch(password):
                user_file.write(f'{email},{password}\n')
            else:
                print("Your password should be atleast 8 characters long!")
        
        else:
            print("Email is not in correct format, Please Check!")
        print("User Registered Successfully")

def login():
    username = []
    password =[]
    data = open('user_detail.txt', 'r')
    for i in data:
        u, p = i.split(",")
        u = u.strip()
        username.append(u)
        password.append(p)
    email = input('Enter Email : ')
    password = input('Enter Password: ')
    if data[username]:
        if password == email:
            print("Hi, You Logged In Successfully") 
        else:
            print("email or password is incorrect")
    else:
        print("user doesnot exsist")
    

option = input("Enter the Choice--> register or login: ")
print(option)
if option == "register":
    register()
elif option == "login":
    login()
else:
    print("Type register or login")
