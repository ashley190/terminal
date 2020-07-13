from functions import *
from winelibrary import *
import sys

# verify age and get name
# print(welcome)
# check_age()
# name = name()
# print(f"Thank you, {name}. Let's select some wine!\n")
code = []

who_for =  select("W")
print("")
#wine selection
if who_for == "W1":
    reason = select("R")
    code.append(reason)
    if reason == "R2":
        dinner = select("D")
        code.append(dinner)
        if dinner == "D1":
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)").lower())
            if boxed_wine == "y":
                code.append("BW")
        if dinner == "D3":
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)").lower())
            if sommelier == "y":
                code.append("S")
    if reason == "R5":
        old_new_world = select("ONW")
        if old_new_world == "ONW1":
            code.append("OLD")
        elif old_new_world == "ONW2":
            code.append("NEW")
if who_for == "W2":
    reason_2 = select("SR")
    if reason_2 == "SR1":
        care = select("C")
        code.append(care)
    elif reason_2 == "SR2":
        deserve = valid_y_n(input("Are they good people deserving of wine?\n(y/n)").lower())
        if deserve == "y":
            know = valid_y_n(input("Do you know what they like?\n(y/n)").lower())
            if know == "y":
                code.append("KNOW")
            elif know == "n":
                code.append("DONTKNOW")
        elif deserve == "n":
            code.append("R7")

summary = f"{name} {purpose[code[-1]]}"
print(summary)

search = wine_list[code[-1]]
print(search)
print(description[search[0]][0])

# for value in search:
#     print(f"""
#     {value}
#     Description: {description[value[0]]}
#     Food pairing: {description[value[1]]}
#     Alternative(s): {description[value[2]]}
#     """)
        

