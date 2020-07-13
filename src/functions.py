import sys
from winelibrary import options

welcome = """
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-
1. When prompted for your input, type in the required information/choices and press "return"/"enter.
2. Emergency exit: To exit this application, please press 'Ctrl+C'.
But before we proceed, please confirm your age.
"""

def check_age(): #age check function
    age = input("Age: ")
    while not age.isnumeric():
        age = input("Please enter numbers only: ")

    if int(age) < 18: 
        sys.exit("Come back when you're older")
    else:
        return

def name(): 
    name = input("Enter your name: ")
    confirm = input(f"Your name is {name}, is that correct?)\n(y/n) ").lower()
    confirm = valid_y_n(confirm)
    code = []

    while confirm == "n":
        name = input("What is your name and press 'return/enter' when done.\n")
        confirm = valid_y_n(input(f"Your name is {name}, is that correct?\n(y/n) ").lower())
    return name

def select(key):
    for text in options[key]:
        print(text)
    selection = key + valid(input("Select one: "),len(options[key])-1)
    return selection

def valid_y_n(x):
    x = x.lower()
    valid_entries = {"y", "n"}
    while x not in valid_entries:                                                                                           
        x = input("Please enter 'y' or 'n'.\n(y/n) ").lower()
    return x

def valid(x, y):
    x.strip()
    options = "(" + f""
    index = range(1, y+1)
    for i in index:
        if i < len(index): 
            options += f"{i}/"
        elif i == len(index):
            options += f"{i})"
    
    while not x.isnumeric() or x.isspace() or int(x) not in range(1, y+1):
        print("Please enter a valid option")
        x = input(options)
    return x

