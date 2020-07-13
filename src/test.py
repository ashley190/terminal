# Feature 2: Wine selection process
if for_whom == "1":
    code += ["W1"]
    print(f"""Tell me more, {name}. Is this for:-
1 - Drinking solo
2 - To go with my dinner
3 - Looking for a celebratory drink
4 - Just want something suitable for regular drinking
5 - Looking for something to cellar""")
    reason = valid(input("Choose the most suitable option: "), 5)
    if reason == "1":
        code += ["R1"]
        print("wines for solo drinking")
    elif reason == "2":
        code += ["R2"]
        print(f"""How fancy is dinner?
1 - Budget dinner at home/takeout
2 - Cooking something nice and want something that is good to cook with and drink
3 - Fancy dinner""")
        dinner = valid(input("Choose the most suitable option: "), 3)
        if dinner == "1":
            code += ["D1"]
            boxed_wine = valid_y_n(input("Will boxed wine do?\n(y/n)"))
            if boxed_wine == "y":
                code += ["BW"]                  
                print("Boxed wine it is!")
            elif boxed_wine == "n":
                print("wines for solo drinking")
        elif dinner == "2":
            code += ["D2"]
            print("wines for cooking and drinking")
        elif dinner == "3":
            code += ["D3"]
            sommelier = valid_y_n(input("Is a sommelier/wine connoiseur present?\n(y/n)"))
            if sommelier == "y":
                code += ["S"]
                print("The sommelier should take over from here.")
            else:
                print("wines for fancy dining out")
    elif reason == "3":
        code += ["R3"]
        print("celebratory wine")
    elif reason == "4":
        code += ["R4"]
        print("wines for regular drinking")
    elif reason == "5":
        code += ["R5"]
        print("""
1 - Old World - I am a traditionalist
2 - New World - I am a modernist
3 - Both - I don't discriminate""")
        old_or_new = valid(input("Your choice: "), 3)
        if old_or_new == "1":
            code += ["OLD"]
            print("old world wines")
        elif old_or_new == "2":
            code += ["NEW"]
            print("new world wines")
        else:
            print("both old and new world wines")
elif for_whom == "2":
    code += ["W2"]
    print("""Tell me more, {name}, is this for:-
1 - A dinner party?
2 - A gift?""")
    reason = valid(input("Choose the most suitable option: "), 2)
    if reason == "1": 
        code += ["R6"]
        print("""How much do you care about said dinner party?
1 - Not at all. Just a courtesy drink.
2 - A little bit/much more than option 1""")
        care = valid(input("Level of care: "), 2)
        if care == "1":
            code += ["C0"]
            print("""There are 3 options:-
1 - two buck chuck
2 - pick something random with an attractive label suited to your budget if you don't want to look cheap
3 - buy something else?
            """)
        if care == "2": 
            code += ["C1"]
            print("""
1 - Care a little - red blend
2 - Care a lot - A good bottle of Pinot Noir never disappoints
            """)
    if reason == "2":
        code += ["R7"]
        deserving = valid_y_n(input("Are they good people deserving of wine?\n(y/n)"))
        if deserving == "y":
            know = valid_y_n(input("Do you know what they like?\n(y/n)"))
            if know == "y":
                code += ["KNOW"]
                print("Buy something they like within your budget")
            elif know == "n":
                code += ["DONTKNOW"]
                print("Suitable gifting wines")
        elif deserving == "n":
            print("""There are 3 options:-
1 - two buck chuck
2 - pick something random with an attractive label suited to your budget if you don't want to look cheap
3 - buy something else?
            """)

purpose_statement = f"{name} " + match_code(code, purpose)
print(purpose_statement)
print("Thinking.....")

wine_selection = match_code(code, wine_list)


print("Wine Assistant exited")
