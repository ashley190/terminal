#This has all functions used in main.py

def valid_yes_no(x):                                                             #check for valid y/n entry 
    valid_entries = {"y", "n"}
    while x not in valid_entries:                                                                                           
        x = input("Please enter 'y' or 'n'.\n(y/n) ")
    return x

def valid_1_2(x):
    valid_entries = {"1", "2"}
    while x not in valid_entries:
        x = input("Please enter '1' or '2'.\n ")
    return x
