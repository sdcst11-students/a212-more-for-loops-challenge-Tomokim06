#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

for i in range(3):
    username = input("Enter username: ")
    pswd = input("Enter password: ")
    if username == "annie" and pswd == "12345" or username == "betty" and pswd == "password" or username == "charles" and pswd == "iloveyou" or username == "doug" and pswd == "mom" or username == "eddie" and pswd == "default" or username == "flon" and pswd == "0":
        print("Access Granted.")
        break
    else:
        print("Access Denied.")
    print("Try Again!")
else:
    print("No more attemps.")