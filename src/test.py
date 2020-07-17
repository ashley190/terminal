from functions import *
from winelibrary import *
import sys

if "--about" in sys.argv:
    print("""
    Application: The Personal Wine Assistant
    Creator: Ashley Lam
    Purpose: To help users select appropriate wines for appropriate occasions
    Conditions: No access for persons below legal drinking age
    Credits: Wine Folly wine selection chart(https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize)
    """)

if "--help" in sys.argv:
    print(f"""
    The application will prompt for input at each step. Type in your input and press {text_1} at each point.
    exit:   You can exit the application by typing in {text_3}. Exit can be used at all points in the application EXCEPT for y/n steps.
    b:      During the wine selection process, entering {text_2} will enable stepping back through the selection process by one(1) step at a time. 
            {text_2} can continually be used all the way up to the first selection question.
    """)
else:
    print(welcome)
