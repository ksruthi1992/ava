
## AVA

### Table of contents  
* [Project Proposal](https://github.com/CSUS-CSC-131-Fall2017/ava/blob/master/docs/friday-proposal.md)
* [Customer Statement of requirements](https://github.com/CSUS-CSC-131-Fall2017/ava/blob/master/docs/Customer%20Statement%20of%20Requirements.md#customer-statement-of-requirements)
* [Requirements](#requirements)
* [Glossary](#glossary)
* [Functional Requirments](#functional)
  * [Actors and Goals](#actor)
  * [Use Cases](#usecase)
  * [System Sequence Diagrams](#diagrams)

## <a name="requirements"></a> Customer Requirements                                  

| Requirements | Priority | Description                              |
| ------------ | -------- | ---------------------------------------- |
| REQ - 1      | 5        | Ava should be able to authenticate the user/register new users |
| REQ - 2      | 5        | Ava must let users add items to their pantry |
| REQ - 3      | 5        | Ava should be able to find a recipe      |
| REQ - 3a     | 5        | ...based on the ingredients              |
| REQ - 3b     | 4        | ...based on cuisine                      |
| REQ - 3c     | 3        | ...based on time-of-day                  |
| REQ - 4      | 3        | Ava will let users bookmark/save recipes |
| REQ - 5      | 2        | Ava will let users leave a review        |
| REQ - 5a     | 2        | ...by giving a rating (on a scale of 1-5), based on how much they liked it |
| REQ - 5b     | 2        | ...by giving a suggestion in text/comment |
| REQ - 6      | 1        | Ava will let users view recipe of the day and admin should be aple to show recipe of the day to logged in users |
| REQ - 7      | 1        | Ava will let users share their recipes   |
| REQ - 8      | 1        | Ava analyzes recipes and provides related side dishes to make a full meal |
| REQ - 9      | 5        | Admin should be able to add or edit recipes and keep track of most viewed recipes |

## <a name="glossary"></a> Glossary

Ava: the system to be created; she will help a user as they navigate through the site

Pantry: a place to store all of the user's current ingredients; recipes will be found off of this information





## <a name="functionalrequirements"></a> Functional Requirements Specification

### 	<a name="stakeholders"></a> a. Stakeholders

### 	<a name="actor"></a> b. Actors and Goals

<<<<<<< HEAD
### 	<a name="usecase"></a> c. Use Cases

#### 		<a name="casualdescription"></a> i. Casual Description

#### 		<a name="fullydresseddescription"></a> ii. Fully-Dressed Description

#### 		<a name="usecasediagram"></a> iii. Use Case Diagram

​		![image](use_case_diagram.jpg)
=======
![image](diagrams/use_case_diagram.jpg)
>>>>>>> 418360923a5b55a06bb472026ca8878df611c17b





| Use Cases | Description                              |
| --------- | ---------------------------------------- |
| UC - 1    | NewUserSignUp New User can sign up to 'Ava' application |
| UC - 2    | LoginUser Existing user can login to 'Ava' application |
| UC - 3    | SaveIngredients User can save ingredients in the pantry |
| UC - 4    | SearchRecipe User can search recipes based on the search filter |
| UC - 5    | GiveFeedback Existing users can give feedback for recipes |
| UC - 6    | ShareRecipe Users can share recipes on social media |
| UC - 7    | ViewRecipeOfTheDay Users can view recipe of the day |
| UC - 8    | AddRecipe Admin can add recipe           |
| UC - 9    | EditRecipe Admin can edit recipe         |
| UC - 10   | DisplayRceipeOfTheDay Admin can show recipe of the day to logged in users |
| UC - 11   | Authenticate System should be able to validate existing users during login |
| UC - 12   | SearchFilter1 User should be able to search recipe using ingredients |
| UC - 13   | SearchFilter2 User should be able to search recipe using cuisine |
| UC - 14   | SearchFilter1 User should be able to search recipe based on time of the day |
| UC - 15   | FeedbackOption1 Logged in users can provide rating on a scale of 1 to 5 |
| UC - 16   | FeedbackOption2 Logged in users can provide suggestion in text for recipe |
| UC - 17   | ManageAccount Ava should be able to manage specific user account by analyzing recipes and provide related side dishes and let users bookmark or save recipe |
| UC - 18   | TrackMostViewed Admin should be able to track most viewed recipe |

####			<a name="systemrequirements"></a> iv. System Requirements - Use Case Traceability Matrix 

|  Req  	| PW 	| UC1 	| UC2 	| UC3 	| UC4 	| UC5 	| UC6 	| UC7 	| UC8 	| UC9 	| UC10 	| UC11 	| UC12 	| UC13 	| UC14 	| UC15 	| UC16 	| UC17 	| UC18 	|
|:-----:	|:--:	|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|:----:	|:----:	|:----:	|:----:	|:----:	|:----:	|:----:	|:----:	|:----:	|
|  REQ1 	|  5 	|  X  	|  X  	|     	|     	|     	|     	|     	|     	|     	|      	|   X  	|      	|      	|      	|      	|      	|      	|      	|
|  REQ2 	|  5 	|     	|     	|  X  	|     	|     	|     	|     	|     	|     	|      	|      	|      	|      	|      	|      	|      	|      	|      	|
|  REQ3 	|  5 	|     	|     	|     	|  X  	|     	|     	|     	|     	|     	|      	|      	|   X  	|   X  	|   X  	|      	|      	|      	|      	|
|  REQ4 	|  3 	|     	|     	|     	|     	|     	|     	|     	|     	|     	|      	|      	|      	|      	|      	|      	|      	|   X  	|      	|
|  REQ5 	|  2 	|     	|     	|     	|     	|  X  	|     	|     	|     	|     	|      	|      	|      	|      	|      	|   X  	|   X  	|      	|      	|
|  REQ6 	|  1 	|     	|     	|     	|     	|     	|     	|  X  	|     	|     	|   X  	|      	|      	|      	|      	|      	|      	|      	|      	|
|  REQ7 	|  1 	|     	|     	|     	|     	|     	|  X  	|     	|     	|     	|      	|      	|      	|      	|      	|      	|      	|      	|      	|
|  REQ8 	|  1 	|     	|     	|     	|     	|     	|     	|     	|     	|     	|      	|      	|      	|      	|      	|      	|      	|   X  	|      	|
|  REQ9 	|  5 	|     	|     	|     	|     	|     	|     	|     	|  X  	|  X  	|      	|      	|      	|      	|      	|      	|      	|      	|   X  	|

####	###<a name="diagrams"></a> d. System Sequence Diagrams 

Login



![image](diagrams/Sequence_Diagram_for_Login.png)









Add ingredients to Pantry



![image](diagrams/Sequence_Diagram_Input_Ingredients.png)









Search



![image](diagrams/Sequence_Diagram_Search_Recipes_modified.png)





Admin login 



![image](diagrams/Sequence_Diagram_Admin_login.png)



## <a name="nonfunctional"></a> Nonfunctional Requirements

Functionality - 

Usability-

Reliability-

Performance-

Supportability-