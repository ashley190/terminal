from functions import *
from winelibrary import *
import sys

# verify age and get name
# print(welcome)
# check_age()
# name = name()
# print(f"Thank you, {name}. Let's select some wine!\n")

selections = {}
wine_list = 1
code = code_gen()
selections[wine_list] = results(code)

again = valid_y_n(input("Would you like to select more wine?\n(y/n)").lower(), False)
while again == "y": 
    wine_list += 1
    code = code_gen()
    selections[wine_list] = results(code)
    again = valid_y_n(input("Would you like to select more wine?\n(y/n)").lower(), False)

