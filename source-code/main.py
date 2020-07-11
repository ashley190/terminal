from functions import *
from winelibrary import *

#Introduction and brief user guide
print("""
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-
1. When prompted for your input, type in the required information/choices and press "return"/"enter.
2. Emergency exit button: To exit this application, please press Ctrl + C
""")

# Feature 1: Ask user for name
print("First things first...")                                                              #prompt for name and validate
name = input("Enter your name: ")
confirm = input(f"Your name is {name}, is that correct?)\n(y/n) ")
confirm = valid_yes_no(confirm)

while confirm == "n":                                                                       #permit name change up till user is happy
    name = input("What is your name and press 'return/enter' when done.\n")
    confirm = valid_yes_no(input(f"Your name is {name}, is that correct?\n(y/n) ").lower()) #validation function imported from functions.py

print(f"Thank you, {name}. Let's select some wine!")                            

# Feature 2: Wine selection process
print(f"""Are you choosing this for yourself or for someone else?
1 - wine for {name}
2 - wine for someone else""")
personal_wine = valid(input("Please select '1' or '2': "), 2)

# if personal_wine == "1":
#     print(f"""Tell me more, {name}. Is this for:-
#     1 - A bit of solo drinking
#     2 - A spot of dinner
#     3 - I just want something suitable for regular drinking
#     4 - Looking for something to put in my cellar
#     5 - Looking for a celebratory drink""")
#     personal_wine_reason = valid_1_5()
    

print("Wine Assistant exited")


