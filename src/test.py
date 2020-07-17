from termcolor import colored, cprint

# text = colored('Hello, World!', 'red', attrs=['underline'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')

strings = ["'return'/'enter'", "b", "exit", "y", "n"]

def format_strings(list):
    for index, string in enumerate(strings):
        return index = colored(string, 'blue', attrs=['bold', 'underline'])

answer = format_strings(strings)
print(answer)

# text_1 = colored("'return'/'enter'", 'blue', attrs=['bold', 'underline'])
text_2 = colored("b", 'blue', attrs=['bold', 'underline'])
text_3 = colored("exit", 'blue', attrs=['bold', 'underline'])
text_4 = colored("y", 'blue', attrs=['bold', 'underline'])
text_5 = colored("n", 'blue', attrs=['bold', 'underline'])

welcome = f"""
Welcome to your personal wine assistant. 
I will help guide you through the often overwhelming process of selecting wine for different situations.
Here are some basic controls for this application:-

1.  When prompted for your input, type in the required information/choices followed by {1} to submit your input. This applies to all inputs.
    If you've entered an invalid input, you will be prompted again to submit a new input.
2.  Special inputs:-
        {text_2} : During the selection process, submit 'b' to go back one step in the selection process.
        {text_3}: Helps you exit the application. You can submit an 'exit' command at any point in the application other than a y/n step. 
                You'll be prompted to confirm your exit by entering y/n. 
                If {text_4} is chosen, the application will exit. 
                If {text_5} is chosen, the application will continue to prompt you for information to proceed at the current step.
                
Let's get started!
"""

print(welcome)
