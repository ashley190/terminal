def valid_y_n(x):
    valid_entries = {"y", "n"}
    while x not in valid_entries:                                                                                           
        x = input("Please enter 'y' or 'n'.\n(y/n) ")
    return x

def valid(x, y):
    x.strip()
    options = "(" + f""
    index = range(1, y+1)
    for i in index:
        if i < len(index): 
            options += f"{i}/"
        elif i == len(index):
            options += f"{i})"
    
    while not x.isnumeric() or x.isspace() or int(x) not in range(1, y+1):
        print("Please enter a valid option")
        x = input(options)
    return x

def match_code(code, library):
    if "BW" in code: 
        return library["BW"]
    elif "S" in code: 
        return library["S"]
    elif "OLD" in code:
        return library["OLD"]
    elif "NEW" in code:
        return library["NEW"]
    elif "D1" in code:
        return library["D1"]
    elif "D2" in code:
        return library["D2"]
    elif "D3" in code:
        return library["D3"]
    elif "R1" in code:
        return library["R1"]
    elif "R3" in code:
        return library["R3"]
    elif "R4" in code:
        return library["R4"]
    elif "R5" in code:
        return library["R5"]
    elif "KNOW" in code:
        return library["KNOW"]
    elif "DONTKNOW" in code:
        return library["DONTKNOW"]
    elif "R7" in code:
        return library["R7"]
    elif "C0" in code:
        return library["C0"]
    elif "C1" in code:
        return library["C1"]

