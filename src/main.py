#!/usr/sbin/python

from functions import *
from winelibrary import *
import sys

if "--about" in sys.argv and "--help" in sys.argv:
    print(about_txt)
    print(help_txt)
elif "--about" in sys.argv:
    print(about_txt)
elif "--help" in sys.argv:
    print(help_txt)
else:
    print(welcome)
    check_age()
    name = name()
    print(f"Thank you, {name}. Let's select some wine!")

    selection = wine_select(name)
    # print(selection)

    if len(selection) > 1:
        print("Here are all the wines we picked today...")
        for item in selection:
            print(selection[item][0])
            print(selection[item][1])
    print("Enjoy!")
