from functions import *
from winelibrary import *
import sys

# verify age and get name
# print(welcome)
# check_age()
# name = name()
# print(f"Thank you, {name}. Let's select some wine!\n")

wine = 1

code = code_gen()
results(code)

another_wine = input("Is there anything else I can help with today?\n(y/n)")
