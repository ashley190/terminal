#This has all functions used in main.py

def valid_yes_no(x):                                                             #check for valid y/n entry 
    valid_entries = {"y", "n"}
    while x not in valid_entries:                                                                                           
        x = input("Please enter 'y' or 'n'.\n(y/n) ")
    return x

def valid(x, y):
    while int(x) not in range(1, y+1):
        x = input("Please enter a valid option.\n ")
    return x


