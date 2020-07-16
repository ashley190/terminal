import sys
from winelibrary import *
from prettytable import PrettyTable, PLAIN_COLUMNS

welcome = """
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-

1. When prompted for your input, type in the required information/choices and press "return"/"enter.
2. Emergency exit: To exit this application, please press 'Ctrl+C'.
3. To go back to the previous step during the selection process 
But before we proceed, please confirm your age.
"""

def check_age(): #age check function
    age = input("Age: ")
    while not age.isnumeric():
        age = input("Please enter numbers only: ")

    if int(age) < 18: 
        sys.exit("Come back when you're older. Goodbye!")
    else:
        return

def name(): 
    name = input("Enter your name: ")
    confirm = input(f"Your name is {name}, is that correct?)\n(y/n) ").lower()
    confirm = valid_y_n(confirm, False)

    while confirm == "n":
        name = input("What is your name and press 'return/enter' when done.\n")
        confirm = valid_y_n(input(f"Your name is {name}, is that correct?\n(y/n) ").lower(), False)
    return name

def select(key):
    for text in options[key]:
        print(text)
    user_input = valid(input("Select an option: "),len(options[key])-1)
    if user_input == "b" or user_input == "f":
        return user_input
    else:
        selection = key + user_input
        return selection


def valid(x, y):
    x.strip()
    options = "(" + f""
    index = range(1, y+1)
    for i in index:
        if i < len(index): 
            options += f"{i}/"
        elif i == len(index):
            options += f"{i})"
    if x.lower() == "b" or x.lower() == "f":
        return x.lower()
    else: 
        while not x.isnumeric() or x.isspace() or int(x) not in range(1, y+1):
            print("Please enter a valid option")
            x = input(options)
        return x

def valid_y_n(x, y=False):
    x = x.lower()
    if y == True:
        valid_entries = {"y", "n", "b"}
        while x not in valid_entries:                                                                                           
            x = input("Please enter 'y' or 'n' or 'b' to go back.\n(y/n) ").lower()
        return x
        
    elif y == False: 
        valid_entries = {"y", "n"}
        while x not in valid_entries:                                                                                           
            x = input("Please enter 'y' or 'n'.\n(y/n) ").lower()
        return x

def code_gen():
    code = []
    while not code:
        code.append(select("W"))
        if code[-1] == "b":
            code.pop()
    while code[-1] in ["W1", "R2", "D1", "D3", "R5", "W2", "E1", "E2", "b"]:
        if code[-1] == "W1":
            code.append(select("R"))
        elif code[-1] == "R2":
            code.append(select("D"))
        elif code [-1] == "D1":
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)").lower(), True)
            if boxed_wine == "y":
                code.append("BW")
            elif boxed_wine == "n":
                code.append("NBW")
            elif boxed_wine == "b":
                code.pop()
        elif code[-1] == "D3":
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)").lower(),True)
            if sommelier == "y":
                code.append("S")
            elif sommelier == "n":
                code.append("NS")
            elif sommelier == "b":
                code.pop()
        elif code[-1] == "R5":
            code.append(select("ONW"))
        elif code[-1] == "W2":
            code.append(select("E"))
        elif code[-1] == "E1":
            code.append(select("C"))
        elif code[-1] == "E2":
            deserve = valid_y_n(input("Are they good people deserving of wine?\n(y/n)").lower(), True)
            if deserve == "y":
                know = valid_y_n(input("Do you know what they like?\n(y/n)").lower(), True)
                if know == "y":
                    code.append("KNOW")
                elif know == "n":
                    code.append("DONTKNOW")
            elif deserve == "n":
                code.append("R7")
            elif deserve == "b":
                code.pop()
        elif code[-1] == "b":
            last_code = code.pop()
            code[-1] = select(code[-1][0])
    return code

def results(code):
    reason = summary[code[-1]]["Reason"]
    print(f"{name} {reason}")

    wine_list = summary[code[-1]]["Wines"]

    try:
        x = PrettyTable()
        x.field_names = ["Wine", "Description", "Food Pairing", "Alternative(s)"]
        x.align = "l"
        x._max_width = {"Wine": 20, "Description": 80, "Food Pairing": 30, "Alternative(s)": 20}
        for value in wine_list:
            if value != wine_list[-1]:
                x.add_row([f"{value}", f"{description[value][0]}", f"{description[value][1]}", f"{description[value][2]}"])
                x.add_row(["","","",""])
            elif value == wine_list[-1]:
                x.add_row([f"{value}", f"{description[value][0]}", f"{description[value][1]}", f"{description[value][2]}"])
        return(x)
    except KeyError:
        return(value)

