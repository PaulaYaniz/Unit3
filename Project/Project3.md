# Project 3: A mood-tracker application for Yasmina
![image](https://user-images.githubusercontent.com/89135778/220579524-79062314-865f-4003-af22-dac634d9b7a0.png)

## Criteria A: Planning
### Problem definition
Yasmina is a student at UWC ISAK Japan. Every Monday morning at her advisory, she fills out the Komodo survey, a survey that checks the students' wellbeing at her school. However, she feels like the survey has too many questions, it is sometimes not accurate enough, and it does not allow her to express all her feelings. She would like to write a personal diary, but as she lives with 3 roommates, she thinks she would not have enough privacy. She would like to be able to write about her feelings every day, and then to have a way to organize the writings by category, according to what she is talking about.

#### Design statement
I will design and make an application for writing a mood diary for a client who is a student at UWC ISAK Japan. The program will consist on an application for being able to keep track of her mood every day, plus being able to write some notes and having them organized by feeling. It is constructed using the softwares Python, Kivy, and SQL. It will take 3 weeks to make and will be evaluated according to the criteria A, B, C, and D.

### Proposed solution
The application will have a sign up and login system with encrypted password, to increase security. The application will be minimalistic and simple for it to be user-friendly. Once the user has passed the login system, a main menu will appear. There, user will be able to select and emotion and write how she is feeling. She can also access past notes organised in folders by emotion. The tools I am using for this are Python, Kivy, and SQL.
I chose Python because  its codes can be easily written and executed much faster than other programming languages[^1]. Python is an open source and has a lot of libraries to complement the code[^2], so there are multiple options of personalisation for fulfilling the client's necessities. Python is also good for the client, as it is free and Yasmina will not need to buy a license[^3].
I chose Kivy because it is also free and convenient for the client, as it can run in many platforms. Kivy is also one of the better front-end softwares. xxx
I chose SQL because it is an easy and simple way to look and get all data.

[^1]: “Advantages of Python over Other Programming Languages.” Vilmate, 2019, https://vilmate.com/blog/python-vs-other-programming-languages/. 
[^2]: “About Python.” Python.org, https://www.python.org/about/. 
[^3]: Citation needed


### First meeting - 10th February 2023
My client and me reunited in a 10-minute meeting.
She wants a mood tracker app. 
Log in and register
Memory problems, so reset forgotten password option

Main page with a box asking what is your mood today?
You can only answer with one word: Sad, happy, depressed, anxious, excited. List of options, you click one.

Notes screen. Every adjective has a different folder in which she writes. She writes in the page she has the feeling.

For bad adjectives, encrypted. New TOP SECRET password that you cannot change. It only has a password hint.

Delete, add, edit notes options.


### Success criteria:
1. There is a secure registration and login system.
2. There is an option to reset forgotten password.
3. The application contains a main page with a box asking what is her mood today, to which she can only answer with one adjective.
4. After answering the adjective, costumer will be able to write notes.
5. The notes will be grouped in folders by the adjectives.
6. Negative adjectives notes will be encrypted, and password cannot be changed.
7. The application will allow to delete, add and edit notes.

![image](https://user-images.githubusercontent.com/89135778/220805673-657a1824-1ded-4267-ae6a-34af9c249100.png)


### Things to be done:
- Wireframe diagram
- Database ER diagram
- RoT up to date
- some code

 # Criteria B: Design

## Test Plan
| Test | Description | Procedure | Expected Output |
|:----:|:-----------:|:---------:|:---------------:|

## System Diagram

**Figure 1:** System diagram of my project

Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (main, login, website_data and proj_lib). Then, these codes connect with a database of csv files (data_transactions and login).

## Flow Diagrams

## Record of Tasks (make it chronological!)

## Record of Tasks
**Task No**|**Planned Action**|**Planned Outcome**|**Time estimate**|**Target completion date**|**Criterion**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
1|First meeting with client|Client described her requiremetns for the project|10min|Feb 10|A
2|Second meeting with client|Write Success Criteria and Client gives her agreeing|10min|Feb 20|A
3|Write the problem context|Problem definition|10min|Feb 20|A
4|Write proposed solution|Have a better understanding of what I have to do and write design statement|15min|Feb 22|A
5|Create first page|Code first page, which contains login and singup buttons|45min|Feb 28|D?
6|Create sign up page|Code sign up and database|1h|Feb 28|D?
7|Create log in page|Code log in and connect it to database|1h|Feb 28|D?
8|Make prototype|Draw a digital protoype|2h|Mar 1|C?

**Table 1:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development (criterias A, B and C). The target completion date and the time estimate for each task is also shown.

# Criterion C

