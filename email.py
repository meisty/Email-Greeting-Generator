import pyperclip
from datetime import datetime as dt
import time
import os

#Function to get the recipients name
def Getname():
    name=input("Please enter the name:  ")
    return name

#Generate the menu which the user can make their selection from
def Generate_menu():
    print("-" * 38)
    print("\n")
    print("   Email Generator Tool version 1.0")
    print("   Author: Shaun Dixon\n   Released: 16/05/2017")
    print("\n")
    print("-" * 38)
    print("1.   First contact general email")
    print("2.   First contact delayed")
    print("3.   Follow up email")
    print("4.   Follow up email close in 5 days")
    print("5.   Follow up email - Potential first time resolution")
    print("6.   Exit program")
    print("-" * 38)
    print("\n \n")

#Determine the subject of the email
def get_subject():
    subject=input("Please enter the subject you are followng up on:  ")
    return subject

#Generate greeting to either "good morning" or "good afternoon" depending on the system time
def greeting():
    date = dt.now()
    if date.hour < 12:
        return "Good morning "
    else:
        return "Good afternoon "

#Function which determines the text copied to the clipboard
def Choice():
    c = input("Please select one of the above options to proceed:  ")
    if c == '1':
        pyperclip.copy(greeting() + Getname() + ",\n \nThank you for your patience while I have been looking into this further for you." + footer())
    elif c == '2':
        pyperclip.copy(greeting() + Getname() + ",\n \nFirstly let me apologise for the delay in contacting you, we are currently experiencing a high volume of calls however I hope to assist you with a resolution as quickly as possible." + footer())
    elif c== '3':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + "." + footer())
    elif c== '4':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + "." + footer())
    elif c== '5':
        pyperclip.copy(greeting() + Getname() + ",\n \nI am following up on the email I sent you regarding your issue to do with " + get_subject() + "." + footer())
    elif c== '6':
        c = 'y'
    else:
        c = 'error'
    return c

#function which generates the menu, gets user choice and then either exits the program or performs required action
def generate_email_header():
    exit = 'n'
    while True:
        Generate_menu()
        choice = Choice()
        if choice == 'y':
            break
        elif choice == 'error':
            print("\n\n\nSorry I did not recognise your input.  Please select one of the above options.")
            time.sleep(4)
        else:
            print("\n\n\nYour email greeting has been copied to your clipboard.")
            time.sleep(4)
            os.system('clear')

def footer():
    return '\n\n\n\nI hope that this has resolved your issue, if however it has not please contact me and I will reopen the call and investigate further.'


generate_email_header()
