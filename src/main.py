from functions import *
from winelibrary import *
import sys

# verify age and get name
# print(welcome)
# check_age()
# name = name()
# print(f"Thank you, {name}. Let's select some wine!\n")

code = code_gen()
print(code)

reason = summary[code[-1]]["Reason"]
print(f"{name} {reason}")

wine_list = summary[code[-1]]["Wines"]

for value in wine_list:
    try:
        print(f"""
{value}
{"Description:":<18}{description[value][0]:<10}
{"Food pairing:":<18}{description[value][1]:<10}
{"Alternative(s):":<18}{description [value][2]:<10}
        """)
    except KeyError:
        print(value)


