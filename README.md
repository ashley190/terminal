# Wine Assistant Terminal Application

## Objective 
The objective of the Wine Assistant is to provide wine suggestions for different purposes as selected by a user loosely based on the flow chart adopted from [Wine Folly](https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize).

## Target Audience
The intended target audience of this application is for people who:-
* enjoys the occasional bottle/glass of wine
* does not have much knowledge about wines but wants to have something suitable certain occasions
* may or may not have access to a personal sommelier
* need help selecting wine for different preferences or circumstances

## Application Features
1. Age checker - Application will check for user age at the start of the application. If below legal age, app will exit with no option to continue. 
2. Invalid entry checks - where user input needs to be a specific range of values, user entry will be checked for invalid entries and users prompted for input until a valid input is entered.
3. User will be guided through the selection process as laid out in the ![Wine selection control flow](<<link>>). Users can also navigate backwards during the selection process if a selection error is made.
4. Results of the selection will be displayed at the conclusion of the selection process. Results can be a one-liner or a table listing the type(s) of suitable wine, description of each type of wine, suitable food pairing option(s) and suitable alternatives(if available).
5. Users have the option to repeat the selection process for as many purposes as required at the end of each selection process. If more than one selection was made, a summary will be printed before the application exits. 

## User Guide
### Starting up the Wine Assistant Terminal Application
1. Open up the Terminal
2. Navigate to the 'yokemeilam_T1A3/src' folder
3. Type in the command:
    `python main.py`

### Using the Application
1. A welcome message will be printed to the user's terminal with a basic user guide 
2. User will be prompted for his/her age. If below legal age of 18, app will automatically exit. 
3. If above 18, user will be prompted for his/her name. User has the ability to change his/her name until it is confirmed. 
4. Once name is confirmed, wine selection begins, user will be prompted at every stage of the process with either numbered or yes/no options. Invalid options will be checked at every input point and user will be prompted until a valid response is received. 
5. During the selection process, if user enters in 'b' as an input, he/she will be taken to one step back in the selection process and user will be able to correct his/her entry. Users have the ability to go all the way back one-step each time, to the first question in the selection process. 
6. At the end of each selection process, the result(s) will be printed out for the user for that specific purpose.
7. User will be prompted if he or she would like to select wine for another purpose. The selection process will re-initiate again for another purpose and results will display at the end of each selection process. User can repeat the process as many times as required.
8. Once wines have been selected for all of the user's purpose(s), a summary will be printed if more than one purpose was selected before the application prints a goodbye message before exiting.

## File Structure

