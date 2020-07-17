import sys
from winelibrary import *
from prettytable import PrettyTable

welcome = """
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-

1. When prompted for your input, type in the required information/choices and press "return"/"enter".
2. To go back to the previous step during the selection process, type in 'b' and press "return"/"enter".
3. Emergency exit: To exit this application at any time, please press 'Ctrl+C'.
But before we proceed, please confirm your age.
"""

def exit(x, continue_txt):
    if x.lower() == "exit":
        confirm = valid_y_n(input("Are you sure you want to exit this application?\n(y/n)"))
        if confirm == "y":
            sys.exit("Goodbye!")
        elif confirm == "n":
            x = input(continue_txt)
            return x
    else:
        return x

def check_age(): #age check function
    age = exit(input("Age: "),"Please enter your age to continue: ")

    while not age.isnumeric():
        age = exit(input("Please enter your age in whole numbers: "), "Please enter your age to continue: ")

    if int(age) < 18: 
        sys.exit("Come back when you're older. Goodbye!")
    else:
        return

def name(): 
    name = exit(input("Enter your name: "), "Please enter your name to continue: ")

    confirm = input(f"Your name is {name}. Is this correct?\n(y/n) ")
    confirm = confirm.lower()
    confirm = valid_y_n(confirm, False)

    while confirm == "n":
        name = exit(input("Enter your name: "), "Please enter your name to continue: ")
        confirm = valid_y_n(input(f"Your name is {name}. Is this correct?\n(y/n) ").lower(), False)
    return name

def select(key):
    for text in options[key]:
        print(text)
    user_input = valid(input("Select an option: "),len(options[key])-1)
    if user_input == "b":
        return user_input
    else:
        selection = key + user_input
        return selection


def valid(x, y):
    x = x.strip().lower()
    x = exit(x, "Select an option to continue: ")

    options = "(" + f""
    index = range(1, y+1)
    for i in index:
        if i < len(index): 
            options += f"{i}/"
        elif i == len(index):
            options += f"{i})"
    if x == "b":
        return x
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
        try:
            if code[-1] == "b":
                code.pop()
                code[-1] = select(code[-1][0])
        except IndexError:
            while not code:
                print("""
    You are at the start of the selection process. 
    You cannot go back any further. 
    Please select a valid option.""")
                code.append(select("W"))
                if code[-1] == "b":
                    code.pop()
    return code

def results(code, name):
    reason = summary[code[-1]]["Reason"]
    purpose = summary[code[-1]]["Purpose"]
    print(f"{name} {reason}")

    wine_list = summary[code[-1]]["Wines"]

    try:
        print(purpose)
        x = PrettyTable()
        x.field_names = ["Wine", "Description", "Food Pairing", "Alternative(s)"]
        x.align = "l"
        x._max_width = {"Wine": 20, "Description": 60, "Food Pairing": 30, "Alternative(s)": 20}
        for value in wine_list:
            if value != wine_list[-1]:
                x.add_row([f"{value}", f"{description[value][0]}", f"{description[value][1]}", f"{description[value][2]}"])
                x.add_row(["","","",""])
            elif value == wine_list[-1]:
                x.add_row([f"{value}", f"{description[value][0]}", f"{description[value][1]}", f"{description[value][2]}"])
        print(x)
        return purpose, x
    except KeyError:
        print(value)
        return purpose, value

def wine_select(name):
    selections = {}
    wine_list = 1
    code = code_gen()
    selections[wine_list] = results(code, name)

    again = exit(input("Would you like to select more wine?\n(y/n)"), "Would you like to select more wine?\n(y/n)")
    again = again.lower()
    again = valid_y_n(again, False)
    while again == "y": 
        wine_list += 1
        code = code_gen()
        selections[wine_list] = results(code, name)
        again = exit(input("Would you like to select more wine?\n(y/n)"), "Would you like to select more wine?\n(y/n)")
        again = again.lower()
        again = valid_y_n(again, False)
    return selections

