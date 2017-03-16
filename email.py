import pyperclip
from datetime import datetime as dt
import time

def Getname():
    name=input("Please enter the name:  ")
    return name

def Generate_menu():
    print("-" * 38)
    print("\n")
    print("   Email Generator Tool version 1.0")
    print("   Author: Shaun Dixon\n   Released: 25/01/2017")
    print("\n")
    print("-" * 38)
    print("1.   First contact general email")
    print("2.   First contact delayed")
    print("3.   Follow up email")
    print("4.   Follow up email close in 5 days")
    print("5.   Follow up email - Potential first time resolution")
    print("-" * 38)
    print("\n \n")

def get_subject():
    subject=input("Please enter the subject you are followng up on:  ")
    return subject

def greeting():
    date = dt.now()
    if date.hour < 12:
        return "Good morning "
    else:
        return "Good afternoon "

def Choice():
    c = input("Please select one of the above options to proceed:  ")
    if c == '1':
        pyperclip.copy(greeting() + Getname() + ",\n \nThank you for your patience while I have been looking into this further for you.")
    elif c == '2':
        pyperclip.copy(greeting() + Getname() + ",\n \nFirstly let me apologise for the delay in contacting you, we are currently experiencing a high volume of calls however I hope to assist you with a resolution as quickly as possible.")
    elif c== '3':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + ".")
    elif c== '4':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + ".")
    elif c== '5':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + ".\n\nI hope that this has resolved your issue, if however it has not please contact me and I will reopen the call and investigate further.")


Generate_menu()
Choice()
# print("Your email greeting has been copied to your clipboard.\nThis Window will now close")
# time.sleep(4)
