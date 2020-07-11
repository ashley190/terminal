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

while confirm == "n":                                                                       #permit name change up till user is happy
    name = input("What is your name and press 'return/enter' when done.\n")
    confirm = valid_y_n(input(f"Your name is {name}, is that correct?\n(y/n) ").lower()) #validation function imported from functions.py

print(f"Thank you, {name}. Let's select some wine!")                            

# Feature 2: Wine selection process
print(f"""Are you choosing this for yourself or for someone else?
1 - wine for {name}
2 - wine for someone else""")
for_whom = valid(input("Your option: "), 2)

if for_whom == "1":
    print(f"""Tell me more, {name}. Is this for:-
    1 - A bit of solo drinking
    2 - To go with my dinner
    3 - Looking for a celebratory drink
    4 - Just want something suitable for regular drinking
    5 - Looking for something to cellar""")
    reason = valid(input("Choose the most suitable option: "), 5)
    
    if reason == "1":
        print("wines for solo drinking")            #end of logic
    elif reason == "2":
        print(f"""How fancy is dinner?
        1 - Budget dinner at home/takeout
        2 - Cooking something nice
        3 - Fancy dinner out""")
        dinner = valid(input("Choose the most suitable option: "), 3)
        if dinner == "1":
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)"))
            if boxed_wine == "y":                  
                print("Boxed wine it is!")          #end of logic
            elif boxed_wine == "n":
                print("wines fors solo drinking")   #end of logic
        elif dinner == "2":
            print("wines for cooking and drinking") #end of logic
        elif dinner == "3":
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)"))
            if sommelier == "y":
                print("The sommelier should take over from here.")  #end of logic
            else:
                print("wines for fancy dining out") #end of logic
    elif reason == "3":
        print("celebratory wine")                      #end of logic
    elif reason == "4":
        print("wines for regular drinking")             #end of logic
    elif reason == "5":
        print("""
        1 - Old World - I am a traditionalist
        2 - New World - I am a modernist
        3 - Both - I don't discriminate""")
        old_or_new = valid(input("Your choice: "), 3)
        if old_or_new == "1":
            print("old world wines")                    #end of logic
        elif old_or_new == "2":
            print("new world wines")                    #end of logic
        else:
            print("both old and new world wines")       #end of logic
elif for_whom == "2":
     

        



print("Wine Assistant exited")


