#This has all functions used in main.py

def valid_y_n(x):                                                             #check for valid y/n entry 
    valid_entries = {"y", "n"}
    while x not in valid_entries:                                                                                           
        x = input("Please enter 'y' or 'n'.\n(y/n) ")
    return x

def valid(x, y):
    options = "(" + f""
    index = range(1, y+1)
    for i in index:
        if i < len(index): 
            options += f"{i}/"
        elif i == len(index):
            options += f"{i})"
    
    while x.isalpha() or int(x) not in range(1, y+1):
        print("Please enter a valid option")
        x = input(options)
    return x


