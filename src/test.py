from functions import *
from winelibrary import *

def code_gen():
    code = []
    if not code:
        code.append(select("W"))
    while code[-1] in ["W1", "R2", "D1", "D3", "R5", "W2", "E1", "E2", "b","f"]:
        if code[-1] == "W1":
            code.append(select("R"))
        elif code[-1] == "R2":
            code.append(select("D"))
        elif code [-1] == "D1":
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)").lower(), True)
            if boxed_wine == "y":
                code.append("BW")
            elif boxed_wine == "n":
                code.append("NBW")
            elif boxed_wine == "b":
                code.pop()
        elif code[-1] == "D3":
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)").lower(),True)
            if sommelier == "y":
                code.append("S")
            elif sommelier == "n":
                code.append("NS")
            elif sommelier == "b":
                code.pop()
        elif code[-1] == "R5":
            code.append(select("ONW"))
        elif code[-1] == "W2":
            code.append(select("E"))
        elif code[-1] == "E1":
            code.append(select("C"))
        elif code[-1] == "E2":
            deserve = valid_y_n(input("Are they good people deserving of wine?\n(y/n)").lower(), True)
            if deserve == "y":
                know = valid_y_n(input("Do you know what they like?\n(y/n)").lower(), True)
                if know == "y":
                    code.append("KNOW")
                elif know == "n":
                    code.append("DONTKNOW")
            elif deserve == "n":
                code.append("R7")
            elif deserve == "b":
                code.pop()
        elif code[-1] == "b":
            last_code = code.pop()
            code[-1] = select(code[-1][0])
    return code

code = code_gen()
print(code)
