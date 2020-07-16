# Software Development Plan - Wine Assistant Terminal Application
## Terminal application name: Wine selector
### Statement of Purpose and Scope

#### Objective
The main objective of this application make wine type selection more approachable by selecting appropriate type(s) of wine based on a user's circumstances. Suitable of wine can be tailored to reasons such as cooking/pairing with food, social drinking, solo drinking or celebratory drinking etc. Selection flow is adapted from [Wine Folly's Flowchart](https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize). 

#### Target Audience
The intended target audience of this application is for people who:-
* enjoys the occasional bottle/glass of wine
* does not have much knowledge about wines but wants to have something suitable certain occasions
* may or may not have access to a personal sommelier
* need help selecting wine for different preferences or circumstances

#### Problems addressed
This application is intended to educate and assist in selecting appropriate wines for any occasion akin to having a personal digital sommelier. This will help reduce anxiety or feelings of inadequacy for someone who don't consider themself a connoisseur but would still like to select appropriate wine for certain settings. 

#### User Interaction and Experience
User will interface with the application using basic commands within the command shell. The application will prompt user for a name at the beginning and will guide user through the decision making process by presenting options which user will select at every stage making it an interactive process. At the end of the process, user will be presented with the best type of wine(s) that suits the options entered. 

*Error handling* - at each point of the program where the user is prompted for an input, checks will be put in place to ensure the validity of the user entries. While loops can be used to continually prompt users until a valid entry is obtained. 

*User guide* - A user guide can be found in the README.md file documenting steps required to initialise and run the application in the terminal and show examples of the selection process along with how results will be displayed. 

### Features

#### Scope for minimum viable product
For the purposes of this project, a minimum viable product will have the following functionality/features.
1. *Ability for user to input name at the start* - this is to enable a more personalised feel to the application allowing application to remember the user's name and reference that name throughout the application. 
2. *User guided and prompted through the selection process* - User will be guided through the selection process adapted from the [Wine Folly's Flowchart](https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize) using control flow statements throughout and loops where required. Error handling to be implemented at each selection step to ensure accurate prompts are entered.
3. User presented with the type of wine suitable based on their selection along with a short description of the characteristics of the wine type. 

*Optional functionality(good-to-have)* - if time allows
4. From functionality no. 3 - narrow down to individual bottles of wine based on taste preference and or budget from the type given. - not implemented in this version
5. Suggest potential alternatives if user does not like options presented - implemented
 
### Application Control Flow Diagram
![Wine selection control flow](<<link>>)



