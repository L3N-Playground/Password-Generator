
from random import randint
import time


# Introduction
print("******************"); time.sleep(0.5)
print("Password Generator"); time.sleep(0.5)
print("******************"); time.sleep(0.5)


def password(length=8):
    chars = r'qwertzuiopasdfghjklyxcvbnmQWERTZUIOPASDFGHJKLYXCVBNM1234567890'
    mypass = ''
    for i in range(length):
        r = randint(0, len(chars)-1)
        mypass += chars[r]
    return mypass


pw_generator = True
pw_input = True
#Input validation
while pw_generator:
    while pw_input:
        try:
            x = int(input('Enter a number:  \n'))
            pw_input = False
        except:
            print("Only numbers accepted!")
    print('Your Password:  '+ password(x))

    #New choice
    time.sleep(1)
    choice = ""
    while choice not in ("y" ,"n"):
        choice = input("\nNew Password? [y]Yes [n]No  \n")
        if (choice == "n"):
            pw_generator = False
        else:
            pw_input = True

print("Programm ended")
