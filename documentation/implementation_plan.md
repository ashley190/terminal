# Implementation Plan
## Personal Wine Assistant Application - Implementation of the Minimal Viable Product
The Implementation of the Personal Wine Assistant application is based on the definition of the acceptable minimal viable product which has the following features:-
* **Feature 1**: Ability for user to input name at the start and insert user name where possible to give a more personalised feel in the application. 
* **Feature 2**: Wine selection process based on an adapted ![Selection_flow_chart](/documentation/images/flow_chart.jpg) that provides different options of wine for different circumstances. 
* **Feature 3**: Accurate results displayed at the end of each selection process accompanied with their descriptions, food pairing options and suitable alternatives where available. 

### Breakdown and Prioritisation for Minimal Viable Product
The implementation of the application was broken down into the resource gathering phase, coding phase and testing phase for all features. The gathering of resources must be completed by Jul 13 for coding work to begin. The implementation of the coding and testing phase are as laid out below: 

**Features 2 and 3**were considered to make up the largest parts of the minimal viable product and will be developed concurrently as features are interdependent especially in ensuring specific wines are selected for their specific purposes. **Note**: Due dates below indicate the date that feature development and testing must be completed. Prioritisation lies on completing the coding for all three features before proceeding to test the code as a whole. Additional features can be added as long as there was enough time for implementation and testing by the main due dates. 
** Feature 2** was prioritised as the top feature as it is the most specific and is the main crucial feature for the application to fulfill its purpose. It was broken down to the following tasks and was given a due date of **July 16**. Tasks 2, 3, and 4 were to be developed concurrently to be completed and tested by the due date of Feature 2.
1. (Resource gathering)Plan out and simplify wine selection process from the [Wine Folly Wine Selection Chart](https://media.winefolly.com/how-to-choose-wine-infographic.png#fullsize.). *Due Date*: July 11
2. Implement the selection flow based on the adapted flow chart from Task 1 in code. This task will be allocated a minimum of 3 days to complete. *Due Date*: July 16
3. Error checking must be implemented at every selection stage to ensure a valid user input to proceed the the correct downstream stages as well as select the correct wine. This was to be implemented together with Task 2. *Due Date*: July 16
4. Valid options at each stage of the selection is saved onto a list that can be used as a referral to the appropriate library to display selected wines and their descriptors. *Due Date*: July 16.

**Feature 3** was prioritised after the completion of **Feature 2** and given a due date of **July 17**. It was broken down into the following tasks:-
1. (Resource gathering)Establishment of the wine description library with description, food pairing options and suitable alternatives if available. This involved finding information on the internet and populating the description library on the winelibrary module. Due date: Jul 14
2. Once task 1 is completed, coding work to be completed for the correct wines to be referenced for the correct purpose from the outputs of Feature 2. Due date: Jul 17

**Feature 1** was considered a minor feature to be implemented once Feature 2 and 3 were completed. This was given a due date of Jul 17 Tasks that were crucial for the implementation of Feature 1 included: 
1. Prompting user for to enter name that will be stored in a name variable that can be referenced throughout the application where required.
2. Confirmation step to enable user to confirm his/her name. This step will repeat until user confirms his/ her name. 

### Actual implementation
Refer to [Development log](development-log.md) for a day to day log of the project implementation. Here are some highlights of the implementation of this project.
As a summary, the first version of code of all three features were completed by Jul 13. An additional feature (**Feature 4**) for checking age was added on Jul 13. This feature now made up the first step of the application before prompting user for his/her name to check for whether user was above the legal drinking age of 18. 

The code for version 2 was reworked several times to DRY it out on Jul 13. Further rework of Feature 2 code was done when there was time to implement an additional feature(**Feature 5**) to enable backward navigation during the selection process. In order to enable this feature, Feature 2 was reworked to while loop instead of using the original flow control (if and else statements).

The winelibrary in version 3 was completed on Jul 13 and was further DRY-ed on Jul 14 by condensing the purpose and wine list into a single library. Feature 2 also required recalibration to point to the correct reference. Further organisation of the presentation of information on the app was done using the prettytables module on Jul 16. Decision to implement the final feature- **Feature 6** prior to the testing phase of the application. **Feature 6** enabled users to restart the selection process to select wines for more than one purpose. This can be repeated as many times and a summary will be printed once the user has completed all of his/her selection of wines. Implementation of Feature 6 marks the completion of the application with enough time for testing before the due date. Testing of all features were lanned for and completed on Jul 17.

|           | MVP/Additional Feature | Due date | Resource Gathering | Coding | Testing |
|-----------|------------------------|----------|--------------------|--------|---------|
| Feature 1 | MVP                    | Jul 17   | N/A                | Jul 12 | Jul 16  |
| Feature 2 | MVP                    | Jul 16   | Jul 11             | Jul 14 | Jul 17  |
| Feature 3 | MVP                    | Jul 17   | Jul 13             | Jul 15 | Jul 17  |
| Feature 4 | Additional feature     | Jul 17   | N/A                | Jul 13 | Jul 16  |
| Feature 5 | Additional feature     | Jul 17   | N/A                | Jul 14 | Jul 16  |
| Feature 6 | Additional feature     | Jul 17   | N/A                | Jul 16 | Jul 16  |

### Final Product
The final product has a total of 6 features, 3 of which was not originally planned for but was deemed suitable and implementable within the time limit allowed. These features include:-
**Feature 4** - An age checking feature that acts as a gatekeeper preventing the use of the application by person(s) under the legal drinking age of 18. 
**Feature 5** - A move backwards navigational feature incorporated into Feature 2 allowing users to navigate backwards one step at a time all the way back to the first selection step. Users will not be able to proceed beyond the first selection step.
**Feature 6** - Selection of multiple wines for multiple purposes enabled. All selections will be stored in the application and summarised at the end of all selections. 
