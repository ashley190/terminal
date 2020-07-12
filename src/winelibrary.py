purpose = {
    "R1" : "is looking for wine suitable for drinking solo.", 
    "BW" : "is happy with boxed wine.",
    "D1" : "is looking for wine suitable for a simple dinner at home.",
    "D2" : "is looking for wine suitable for cooking and drinking.",
    "D3" : "is dining out somewhere fancy.",
    "S" : "is dining out someplace with a sommelier of with a wine connoiseur friend.",
    "R3" : "is celebrating and looking for something suitable for the occasion.",
    "R4" : "is looking for something suitable for regular drinking.",
    "R5" : "is looking for something to age but impartial to old/new world wines.",
    "OLD" : "is looking for old world wines for cellaring.",
    "NEW" : "is looking for new world wines suitable for ageing.",
    "C0" : "is looking for wine to bring to a dinner party.",
    "C1" : "is looking for wine to bring to an important dinner party.",
    "R7" : "is looking for a gift for an acquaintance.",
    "KNOW": "wants to gift a bottle to someone close",
    "DONTKNOW" : "is looking for a special bottle for someone special."
}

wine_list = {
    "R1" : ["Pinot Noir", "Sangiovese", "Grenache", "Zinfandel", "Shiraz"], 
    "BW" : "Boxed wine it is!",
    "D1" : ["Pinot Noir", "Sangiovese/Grenache", "Zinfandel/Shiraz"],
    "D2" : ["Cabernet Sauvignon", "Sauvignon Blanc"],
    "D3" : ["Sangiovese/Grenache", "Cotes du Rhone", "Cabernet Sauvignon"],
    "S" : "I would suggest talking to the sommelier/your connoiseur friend.",
    "R3" : ["Bubbly", "Sparkling wine", "Riesling, Merlot", "Pinot Noir"],
    "R4" : ["Malbec", "Chinon/Bourgueil", "Chardonnay"],
    "R5" : ["Bordeaux", "Burgundy", "Rioja", "Riesling", "Pinot Noir", "Shiraz", "Malbec"],
    "OLD" : ["Bordeaux", "Burgundy", "Rioja"],
    "NEW" : ["Riesling", "Pinot Noir", "Shiraz", "Malbec"],
    "C0" : """
    Here are some suggestions:-
    Option 1: 2 buck chuck
    Option 2: Pick a random bottle suited to your budget with a fancy label
    """,
    "C1" : ["Red blend", "Pinot Noir"],
    "R7" : """
    Here are some suggestions:-
    Option 1: 2 buck chuck
    Option 2: picking a random bottle suited to your budget with a fancy label
    """,
    "KNOW": "I would suggest buying a bottle of his/her favorite type within your budget.",
    "DONTKNOW" : ["Pinot Noir", "Pinot Gris", "Sauvignon Blanc"]
    }

description = {
    "Pinot Noir" : """
    Taste               : Very fruity and floral; often with appealing vegetal notes of beet, rhubarb, or mushroom
    Style               : Lighter bodied red
    Description         : Pinot Noir is a dry, light-bodied red that has a higher acidity and a soft, smooth, low-tannin finish.
    Food Pairing        : chicken, pork, veal, duck, cured meats, cream sauces, soft cheeses
    Good alternative(s) : Gamay (Beaujolais)""",

    "Sangiovese" : """
    Taste               : Ranges from rustic to fruity
    Style               : Dry light- to medium-bodied red
    Description         : Italy's most popular grape primarily used in Chianti. Characteristics can vary based on region, climate and the winemaking process.
    Food Pairing        : pizza and pasta with tomato based sauces
    Good alternative(s) : 
    """,

    "Grenache" : """ """,

    "Sangiovese" : """
    Taste: 
    """,

}

print(description["Pinot Noir"])
