options = {
    "W" : ["\nAre you choosing this for yourself or for someone else?", "1 - wine for myself", "2 - wine for someone else"],
    "R" : ["\nTell me more. Is this for:-", "1 - Drinking solo", "2 - To go with my dinner", "3 - Looking for a celebratory drink", "4 - Just want something suitable for regular drinking", "5 - Looking for something to cellar"],
    "E" : ["\nTell me more. Is this for:-", "1 - A dinner party?", "2 - A gift?"],
    "D" : ["\nHow fancy is dinner?", "1 - Budget dinner at home/takeout", "2 - Cooking something nice and want something that is good to cook with and drink", "3 - Fancy dinner"],
    "ONW" : ["\nOld or New World?", "1 - Old World - I am a traditionalist", "2 - New World - I am a modernist", "3 - Both - I don't discriminate"],
    "C" : ["\nHow much do you care about said dinner party?", "1 - Not at all. Just a courtesy bottle.", "2 - A little bit/much more than option 1"]
}

summary = {
    "R1" : 
        {"Reason": "is looking for wine suitable for drinking solo.", 
        "Purpose": "Wines suitable for solo drinking.",
        "Wines": ["Pinot Noir", "Sangiovese/Grenache", "Zinfandel", "Shiraz"]}, 

    "BW" : 
        {"Reason" : "is happy with boxed wine.", 
        "Purpose": "",
        "Wines": ["Boxed wine", "Cleanskin"]},

    "NBW" : {
        "Reason" : "is looking for wine suitable for a simple dinner at home.",
        "Purpose": "Wines suitable for simple home dinners.",
        "Wines": ["Pinot Noir", "Sangiovese/Grenache", "Zinfandel/Shiraz"]},

    "D2" : {
        "Reason" : "is looking for wine suitable for cooking and drinking.", 
        "Purpose": "Wines suitable for cooking and drinking.",
        "Wines": ["Cabernet Sauvignon", "Sauvignon Blanc"]},

    "NS" : {
        "Reason" : "is dining out somewhere nice.", 
        "Purpose": "Wines suitable for fancy dining.",
        "Wines": ["Sangiovese/Grenache", "Cotes du Rhone", "Cabernet Sauvignon"]},

    "S" : {
        "Reason" : "is dining out someplace with a sommelier or with a wine connoiseur friend.", 
        "Purpose": "",
        "Wines": ["I would suggest talking to the sommelier/your connoiseur friend."]},

    "R3" : {
        "Reason" : "is looking for something suitable for a celebration.", 
        "Purpose": "Suitable celebratory wines.",
        "Wines": ["Sparkling wine/Champagne", "Riesling", "Merlot", "Pinot Noir"]},

    "R4" : {
        "Reason" : "is looking for something suitable for regular drinking.", 
        "Purpose": "Wines suitable for regular drinking.",
        "Wines": ["Malbec", "Cabernet Franc", "Chardonnay"]},

    "ONW3" : {
        "Reason" : "is looking for something to age but impartial to old/new world wines.", 
        "Purpose": "Wines for ageing.",
        "Wines": ["Bordeaux", "Burgundy", "Rioja", "Riesling", "Pinot Noir", "Shiraz", "Malbec"]},

    "ONW1" : {
        "Reason" : "is looking for old world wines for cellaring.", 
        "Purpose": "Old world wines for ageing.",
        "Wines": ["Bordeaux", "Burgundy", "Rioja"]},

    "ONW2" : {
        "Reason" : "is looking for new world wines suitable for ageing.", 
        "Purpose": "New world wines for ageing.",
        "Wines": ["Riesling", "Pinot Noir", "Shiraz", "Malbec"]},

    "C1" : {
        "Reason" : "is looking for wine to bring to a dinner party.", 
        "Purpose": "Wines suitable to bring to a dinner party.",
        "Wines": ["Cleanskin"]},

    "C2" : {
        "Reason" : "is looking for wine to bring to an important dinner party.", 
        "Purpose": "Wines suitable to bring to an important dinner party.",
        "Wines": ["Red blend", "Pinot Noir"]},

    "R7" : {
        "Reason" : "is looking for a gift for an acquaintance.", 
        "Purpose": "Wines suitable for gifting.",
        "Wines": ["Cleanskin"]},

    "KNOW": {
        "Reason" : "wants to gift a bottle to someone close", 
        "Purpose": "",
        "Wines": ["I would suggest buying a bottle of his/her favorite type within your budget."]},

    "DONTKNOW" : {
        "Reason" : "is looking for a special bottle for someone who matters.", 
        "Purpose": "Wines suitable for gifting to someone who matters.",
        "Wines": ["Pinot Noir", "Pinot Grigio/Gris", "Sauvignon Blanc"]}
}

description = {
    "Pinot Noir" : ["Pinot Noir is a dry, light-bodied red that has a higher acidity and a soft, smooth, low-tannin finish. It is considered a lighter bodied red that is fruity and floral.", "Pinot Noirs are particularly versatile when it comes to food pairing and can go with a variety of food, duck being a popular pairing. Other foods can range from white to red meats, dishes with cream sauces and cheese like Gruyere.", "Gamay (Beaujolais)"],
    
    "Sangiovese/Grenache" : ["Sangiovese is Italy's most popular grape primarily used in Chianti. Its characteristics can vary based on region, climate and the winemaking process and therefore its taste can range from rustic to fruity. This is a dry light to medium-bodied red with a high acidity. Meanwhile, Grenache is a rich, flavorful red wine originating from Spain with flavors of strawberries, plum, leather, herb and citrus.", "Sangiovese goes well with pizza and pasta, tomato-based dishes like ragu and osso bucco while Grenache goes well with roasted meats and vegetables.", "Zinfandel"],
    
    "Shiraz" : ["Shiraz (also known as Syrah) is a full-bodied red with intense fruit flavors and medium tannins. It often has a savory, spicy, meaty character often with notes of blueberry, plum, pepper, tobacco and violet.", "Goes well with meats, smoked meats, stews and hard cheeses.", "Malbec, Zinfandel"],

    "Zinfandel" : ["Zinfandel is a medium-bodied, fruity and spicy red with a medium length finish. Its taste encompasses a broad array of of fruits from stone fruits to berries (red, blue or black) as well as hints of spice and tobacco.","Goes well with BBQ meats, curries, Indian, Chinese and Thai food as well as firm cheeses such as Manchego.", "Shiraz, Grenache, Temperanillo, GSM/Rhone Blend"],

    "Cotes du Rhone" : ["Cotes du Rhone are wines originating from the specially protected wine growing region in Rhone. Wines originating from the Cotes du Rhone are usually easy drinking and food friendly.", "Great for pairing with most food. General guides: pair white wine with white meat, and red wines with heavier foods.", " "],

    "Cabernet Sauvignon" : ["Cabernet Sauvignon is the most popular wine variety in the world. It is a full-bodied, red with tasting notes of cherry, currant, spices and cedar with bold tannins.", "Goes well with red meats, smoked meats and firm cheeses like aged cheddar or Pecorino. A medium priced bottle is most suitable for cooking and drinking.", "Merlot, Malbec, Cabernet Franc, Bordeaux Blend"],

    "Sauvignon Blanc" : ["Sauvignon Blanc is a dry white wine that has a tart, green profile. Its taste is heavily citrus driven with hints of fruit(melon, passionfruit, kiwi) and herbs such as grass and mint.", "Pairs well with white meats(fish, pork, chicken), Mexican and Vietnamese food, as well as nutty cheeses like Gruyere. It is also suitable to be used in cooking.", "Vermentino"],

    "Sparkling wine/Champagne" : ["""Sparkling wine can come in 4 different styles ranging from dry and zesty to creamy and nutty. 
Dry and zesty sparkling wines are made from cool-climate Chardonnay and Pinot Noir grapes. Wines that fall into this category include most non-vintage(NV) Champagne, Most Cava and Most Brut. 

Light, Fruity and Floral style wines come from warmer climates. Examples of wines in this style include most Brut, extra dry prosecco and sparkling rose.\

Sweet and perfumed wines are made with aromatic grapes like Muscat. Examples of these are Dry Prosecco, Demi-Sec and Doux, Amabile and Dolce.

Rich, Creamy and Nutty are more expensive to make and thus is reflected in their prices. Examples include Reserva and Gran Reserva Cava as well as Vintage CHampagne.""", "", ""],

    "Riesling" : ["Riesling is a floral and fruit driven dry(acidic) white with heavy citrus and stone fruit features as well as floral and sweet herbal elements.Its sweetness can vary depending on the winemaker.", "Pairs well with Indian, Thai, Vietnamese, German and Moroccan food. Can be paired with chicken, pork, duck, turkey, cured meats and fondue", "Moscato, Gewurztraminer, Chenin Blanc"],

    "Merlot" : ["Merlot is a medium to full-bodied red known for its boisterous flavors of black cherry, supple tannins and a chocolatey finish. The body of Merlot can differ based on whether it is cool or warm climate with differences ranging from medium bodied (cool climate) to full-bodied (warm climate).", "Pairs well with a variety of foods and can be open to experimentation. A general guide is to pair easy drinking Merlots with easy food such as pizzas or bbq chicken and heavier Merlots with heavier dishes such as braised meat, roast or beef short rib. Stay away from pairing with fish, salads and spicy dishes.", "Cabernet Sauvignon"],

    "Malbec" : ["Malbec is a full bodied wine loved for their rich, dark fruit flavors and a smooth chocolatey finish. It has a distinctive dark purple colour and notes of red plum, blueberry, vanilla, cocoa and tobacco.", "Goes well with leaner red meats, steak with chimichurri and blue cheese.", "Shiraz, Cabernet Sauvignon"],

    "Cabernet Franc" : ["Cabernet Franc is a medium-bodied, dry red wine originating from the Loire valley in France with aromas of raspberry, bramble and peppers.", "The higher acidity of Cabernet Franc goes well with tomato based dishes or vinegar based sauces (smoky BBQ).", ""],

    "Chardonnay" : ["Chardonnay is a dry medium to full-bodied white wine. Depending on whether it has been aged in oak, its flavor can range from light and zesty (unoaked) to spicy and bourbon-y(oaked). Chardonnay often has a taste profile with citrus, pears and apples, tropical fruits with a touch of butterscotch, fanilla or toasted caramel from oak.", "Pairs very well with seafood and white meats, dishes with cream sauces and cheeses such as brie and Gruyere.", "Semillon, Viognier"],

    "Bordeaux/Burgundy" : ["Known as the two most influential wine regions in the world, Bordeaux and Burgundy wines are named for their place of origin rather than the type of grapes the wine is made from. Bordeaux wines can differ based on whether they are from the left-bank, right-bank or, entre-deux-mers(between two seas). Left bank wines tend to have more prominent tannins and are therefore more ageworthy while right bank wines are silkier and fruitier making them more approachable. Bordeaux wines tend to be more balanced and pairs well with food. Winemaking in Burgundy is guided by the concept of terroir(soil types, weather patterns and geographical conditions) and wines from different parts of Burgundy can have different profiles. Burgundy is known for its Chardonnay and Pinot Noir grapes with bright acidity and mineral notes.", "", ""],

    "Rioja" : ["Rioja is Spains most famous regional wine made with Temperanillo grapes. They are known for their savory dusty flavors and ageability. It is considered a medium to full bodied wine with tasting notes of cherry, plum, dill and vanilla.", "Pairs well with lamb, chorizo, roasted pork or chicken.", "Temperanillo"],

    "Red blend" : ["A red blend wine is wine made from not from a particular type of grape but a combination of more than one grape type. This allows winemakers to 'design' wine blending grapes of different characteristics to form wine that is greater than the sum of its parts. Reasons for blending does not have to be limited to taste but can also take into consideration production and price as well and therefore we can see relatively inexpensive red blend on the market.", "", ""],

    "Pinot Grigio/Gris" : ["Pinot Grigio and Gris comes from the same types of grapes but can differ slightly to each other. Pinot Grigio is a dry light-bodied white wine with delicate citrus, pomaceous fruits and white floral notes while Pinot Gris are more full-bodied, richer and more viscous in texture. Pinot Grigio is known to be easy drinking with a bitter flavor on the palate.", "Pairs well with salad, poached fish, light and mild cheeses. Pinot Gris in contrast pairs well with slightly heartier foods such as veal, rabbit, roasts, casseroles and hard cheeses.", " "],

    "Boxed wine" : ["Wine packaged in a box. This is an inexpensive and more environmentally friendly option. Wine can be consumed within 3-4 weeks after opening as it is less susceptible to oxidation but will recommend consuming within the shelf life indicated by the manufacturer. Just like not all bottled wines are good, the same analogy can be applied to say that not all boxed wine are bad so it is perfectly acceptable as a go to for inexpensive, larger volume consumption.", "", ""],

    "Cleanskin" : ["Wine whose lable does not indicate the winery or winemaker's name but rather only show the grape variety and year of bottling. They are typically sold at a lower price. Cleanskin wines can be originally branded wines sold at a higher price and relabelled as cleanskins or wine specifically made to be sold as cleanskins and therefore the quality of cleanskin wines can vary significantly. So take a pick - there can be an occasional gem in there somewhere.", "", "Pick a random bottle suited to your budget with a fancy label if you're worried about looking cheap."]
}
