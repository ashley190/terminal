#!/usr/sbin/python

from functions import *
from winelibrary import *
import sys

# prints out different text for --about and --help arguments in sys.argv
if "--about" in sys.argv and "--help" in sys.argv:
    print(about_txt)
    print(help_txt)
elif "--about" in sys.argv:
    print(about_txt)
elif "--help" in sys.argv:
    print(help_txt)
else:
#if no argments entered, start main program

#prints welcome message, age check and obtain user name
    print(welcome)
    check_age()
    name = name()
    print(f"Thank you, {name}. Let's select some wine!")

#main body of the program. If more than one selection done, prints out a summary for user.
    selection = wine_select(name)

    if len(selection) > 1:
        print("Here are all the wines we picked today...")
        for item in selection:
            print(selection[item][0])
            print(selection[item][1])
    print("Enjoy!")
