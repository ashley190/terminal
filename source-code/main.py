from functions import *
from winelibrary import *

#Introduction and brief user guide
print("""
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-
1. When prompted for your input, type in the required information/choices and press "return"/"enter.
2. Emergency exit button: To exit this application, please press 'Ctrl+C'
""")

# Feature 1: Ask user for name
print("First things first...")                                                              #prompt for name and validate
name = input("Enter your name: ")
confirm = input(f"Your name is {name}, is that correct?)\n(y/n) ")
confirm = valid_y_n(confirm)
code = []

while confirm == "n":                                                                       #permit name change up till user is happy
    name = input("What is your name and press 'return/enter' when done.\n")
    confirm = valid_y_n(input(f"Your name is {name}, is that correct?\n(y/n) ").lower())    #validation function imported from functions.py

print(f"Thank you, {name}. Let's select some wine!")                            

# Feature 2: Wine selection process
print(f"""Are you choosing this for yourself or for someone else?
1 - wine for {name}
2 - wine for someone else""")
for_whom = valid(input("Your option: "), 2)

if for_whom == "1":
    code += ["W1"]
    print(f"""Tell me more, {name}. Is this for:-
1 - Drinking solo
2 - To go with my dinner
3 - Looking for a celebratory drink
4 - Just want something suitable for regular drinking
5 - Looking for something to cellar""")
    reason = valid(input("Choose the most suitable option: "), 5)
    if reason == "1":
        code += ["R1"]
        print("wines for solo drinking")            #W1 R1
    elif reason == "2":
        code += ["R2"]
        print(f"""How fancy is dinner?
1 - Budget dinner at home/takeout
2 - Cooking something nice
3 - Fancy dinner""")
        dinner = valid(input("Choose the most suitable option: "), 3)
        if dinner == "1":
            code += ["D1"]
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)"))
            if boxed_wine == "y":
                code += ["BW"]                  
                print("Boxed wine it is!")          #W1 R2 D1 BW
            elif boxed_wine == "n":
                print("wines for solo drinking")   #W1 R2 D1
        elif dinner == "2":
            code += ["D2"]
            print("wines for cooking and drinking") #W1 R2 D2
        elif dinner == "3":
            code += ["D3"]
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)"))
            if sommelier == "y":
                code += ["S"]
                print("The sommelier should take over from here.")  #W1 R2 D3 S
            else:
                print("wines for fancy dining out") #W1 R2 D3
    elif reason == "3":
        code += ["R3"]
        print("celebratory wine")                      #W1 R3
    elif reason == "4":
        code += ["R4"]
        print("wines for regular drinking")             #W1 R4
    elif reason == "5":
        code += ["R5"]
        print("""
1 - Old World - I am a traditionalist
2 - New World - I am a modernist
3 - Both - I don't discriminate""")
        old_or_new = valid(input("Your choice: "), 3)
        if old_or_new == "1":
            code += ["OLD"]
            print("old world wines")                    #W1 R5 OLD
        elif old_or_new == "2":
            code += ["NEW"]
            print("new world wines")                    #W1 R5 NEW
        else:
            code += ["OLD", "NEW"]
            print("both old and new world wines")       #W1 R5
elif for_whom == "2":
    code += ["W2"]
    print("""Tell me more, {name}, is this for:-
1 - A dinner party?
2 - A gift?""")
    reason = valid(input("Choose the most suitable option: "), 2)
    if reason == "1": 
        code += ["R6"]
        print("""How much do you care about said dinner party?
1 - Not at all. Just a courtesy drink.
2 - A little bit/much more than option 1""")
        care = valid(input("Level of care: "), 2)
        if care == "1":
            code += ["C0"]
            print("""There are 3 options:-
1 - two buck chuck
2 - pick something random with an attractive label suited to your budget if you don't want to look cheap
3 - buy something else?
            """)
        if care == "2": 
            code += ["C1"]
            print("""
1 - Care a little - red blend
2 - Care a lot - A good bottle of Pinot Noir never disappoints
            """)
    if reason == "2":
        code += ["R7"]
        deserving = valid_y_n(input("Are they good people deserving of wine?\n(y/n)"))
        if deserving == "y":
            code += ["DSRV"]
            know = valid_y_n(input("Do you know what they like?\n(y/n)"))
            if know == "y":
                print("Buy something they like within your budget")
            elif know == "n":
                print("Suitable gifting wines")
        elif deserving == "n":
            print("""There are 3 options:-
1 - two buck chuck
2 - pick something random with an attractive label suited to your budget if you don't want to look cheap
3 - buy something else?
            """)
print(code)
print("Wine Assistant exited")
