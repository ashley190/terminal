# Software Development Plan - Personal Wine Assistant Terminal Application
## Terminal application name: Wine selector
### Statement of Purpose and Scope

#### Purpose
The main objective of this application make wine selection more approachable by selecting appropriate type(s) of wine based on a user's circumstances. Suitable of wine can be tailored to reasons such as cooking/pairing with food, social drinking, solo drinking or celebratory drinking etc. Selection flow is guided by  ![Selection_flow_chart](/documentation/flow_chart.jpg).

#### Target Audience
The intended target audience of this application is for people who:-
* enjoys the occasional bottle/glass of wine
* does not have much knowledge about wines but wants to have something suitable certain occasions
* may or may not have access to a personal sommelier/friend who knows about wine
* need help selecting wine for different preferences or circumstances

#### Problems addressed
This application is intended to educate and assist in selecting appropriate wines for any occasion akin to having a personal digital sommelier. This will help reduce anxiety or feelings of inadequacy for someone who don't consider themself a connoisseur but would still like to select appropriate wine for certain settings. 

#### User Interaction and Experience
**User guide** - A full user guide can be found in the README.md file documenting steps required to initialise and run the application in the terminal and show examples of the selection process along with how results will be displayed. 

A mini help file is also available to the user by passing the --help argument when initialising the application as well as at the beginning of the application once it is launched.

**User Interaction** - User will interface with the application using basic commands within the command shell. The application will prompt user for the user's age and name at the beginning and will guide user through the decision making process by presenting options which user will select at every stage making it an interactive process. At the end of the process, user will be presented with the best type of wine(s) that suits the options entered. 

**Error handling** - at each point of the program where the user is prompted for an input, checks will be put in place to ensure the validity of the user entries. While loops can be used to continually prompt users until a valid entry is obtained. 

### Features
#### Scope for minimum viable product
For the purposes of this project, a minimum viable product will have the following functionality/features.
1. *Ability for user to input name at the start* - this is to enable a more personalised feel to the application allowing application to remember the user's name and reference that name(where required) throughout the application. 
2. *User guided and prompted through the selection process* - User will be guided through the selection process guided by ![Selection_flow_chart](/documentation/images/flow_chart.jpg) . Control flow statements and loops will be heavily utilised throughout the application. Error handling to be implemented at each selection step to ensure accurate inputs are entered.
3. User presented with a list of wines suitable based on their selection along with a short description of the characteristics of the wine type. A basic list can be used to present the selected wine.

*Additional functionality in this release*
These are functionality considered optional until the minimum viable product is achieved or ideas that came up during the development process  The following are features that are implemented in the current release of the application.
1. Age checker
2. Suggest wine alternatives if user does not like options presented - implemented as part of feature 3.
3. Allow user to undergo multiple rounds of selection to select wines for more than one purpose. If wine is selected for more than one purpose, a summary is displayed at the end for all of the user's selection before exiting the application.
4. Enable user to exit app at any stage in the application - Users are able to type 'exit' at any point (other than y/n points) to exit the application. Changes will not be saved.
5. Cosmetic improvements such as wine list displayed in a table and appropriate help text highlighted to improve user experience. 
 
### Resources/References
1. Winefolly.com. https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize. Published 2020. Accessed July 10, 2020.
2. https://www.facebook.com/WineFolly. Common Types of Wine (top varieties to know) | Wine Folly. Wine Folly. https://winefolly.com/deep-dive/common-types-of-wine/. Published May 18, 2015. Accessed July 12, 2020.
3. Sangiovese Wine - Wine Varieties | Cellarmasters. Cellarmasters.com.au. https://www.cellarmasters.com.au/discover/wine-varieties/sangiovese. Published 2018. Accessed July 12, 2020.
4. McWilliams Admin. Pinot Grigio vs Pinot Gris. McWilliam’s Wines. https://mcwilliams.com.au/blogs/news/pinot-grigio-vs-pinot-gris. Published January 2, 2018. Accessed July 12, 2020.
5. Bordeaux Vs. Burgundy: Battle Of The French Wines. The Upsider. https://theupsider.com.au/bordeaux-burgundy-wines/19422. Published October 21, 2019. Accessed July 12, 2020.
6. Schiessl C. We Need a Better Way to Talk About Red Blends. VinePair. https://vinepair.com/articles/whats-a-red-blend/. Published August 22, 2017. Accessed July 12, 2020.
7. Wikipedia Contributors. Box wine. Wikipedia. https://en.wikipedia.org/wiki/Box_wine#:~:text=Boxed%20wine%20(cask%20wine)%20is,a%20cork%20or%20synthetic%20seal. Published June 22, 2020. Accessed July 12, 2020.
8. Wikipedia Contributors. Cleanskin (wine). Wikipedia. https://en.wikipedia.org/wiki/Cleanskin_(wine). Published September 28, 2019. Accessed July 12, 2020.
