# Project 3: A mood-tracker application for Yasmina
![image](https://user-images.githubusercontent.com/89135778/220579524-79062314-865f-4003-af22-dac634d9b7a0.png)

## Criteria A: Planning
### Problem definition
My client is a student at a local school. After meeting with her (see Appendix A) I learned that very Monday morning at her advisory, she fills out the Komodo survey, a survey that checks the students' wellbeing at her school. However, she feels like the survey has too many questions, it is sometimes not accurate enough, and it does not allow her to express all her feelings. She would like to write a personal diary, but as she lives with 3 roommates, she thinks she would not have enough privacy. She would like to be able to write about her feelings every day, and then to have a way to organize the writings by category, according to what she is talking about. My client needs a cost effective, efficient, and more private way to track her emotions and write about them. 

#### Design statement
I will design and make an application for writing a mood diary for a client who is a student at UWC ISAK Japan. The program will consist on an application for being able to keep track of her mood every day, plus being able to write some notes and having them organized by feeling. It is constructed using the softwares Python, Kivy, and SQLite. It will take 3 weeks to make and will be evaluated according to the criteria A, B, C, and D.

### Rationale for proposed solution
OOP is the programming paradigm.The application will have a sign up and login system with encrypted password, to increase security. The application will be minimalistic and simple for it to be user-friendly. Once the user has passed the login system, a main menu will appear. There, user will be able to select and emotion and write how she is feeling. She can also access past notes organised in folders by emotion. The tools I am using for this are Python, Kivy, and SQL.
I chose Python because  its codes can be easily written and executed much faster than other programming languages[^1]. Python is an open source and has a lot of libraries to complement the code[^2], so there are multiple options of personalisation for fulfilling the client's necessities. Python is also good for the client, as it is free and my client will not need to buy a license[^3].
I chose Kivy because it is also free and convenient for the client, as it can run in many platforms. Kivy is fresh, fast, flexible, and focused. If the client needed to sell her application in the future, doing that would be completely free and she would not have to pay anything to Kivy. [^4]
I chose SQLite because it is an easy and simple way to look and get all data. SQLite is lightweight, efficient, and easy to integrate in Python applications.  It does not require a separate server process or system, and data can be stored in a single file, making it easy to manage. The use of Client/Server RDBMS would had been necessary for a high volume website, client/server app, very large databases, and high concurrency of simultaneous readers. [^5] As my app does not have data separated from app by the networks, concurrent writers, or very big data, SQLite is a good option that will meet the client’s requirements.
Overall, the combination of Python, Kivy, and SQLite provides a cost-effective, efficient, and user-friendly solution to the client's needs for a mood tracker application.

[^1]: “Advantages of Python over Other Programming Languages.” Vilmate, 2019, https://vilmate.com/blog/python-vs-other-programming-languages/. 
[^2]: “About Python.” Python.org, https://www.python.org/about/. 
[^3]: Citation needed
[^4]: “Philosophy”, https://kivy.org/doc/stable/philosophy.html
[^5]: “Appropriate Uses For SQLite”, https://www.sqlite.org/whentouse.html

***No need to include a description of the application here since it will come in section B.

### Success criteria:
After meeting with the client ans sending her an email (See Appendix B), we agreed the following success criteria:
1. There is a secure registration and login system with requirements for password and email.
2. The application will contain a page asking how the client is feeling, to which the client will only be able to answer selecting one of the options given.
3. After selecting the feeling, the customer will be able to write notes about it.
4. The notes will be grouped in folders by the adjectives, and will have a date.
5. The application will allow the client to delete and add notes.
6. The application will give statistical information about the user's well-being: number of positive and negative emotions felt.

### Things to be done:
- Wireframe diagram
- Database ER diagram
- RoT up to date
- some code
 # Criteria B: Design
## Test Plan
| Test | Description | Procedure | Expected Output |
|:----:|:-----------:|:---------:|:---------------:|
Code review - quality (non-functional)
Organisations: is everythinh organised? Folders, files, etc. (non-functional)
Unit testing (functional): password policy
UT: Integration: whole login page
6 sucess criteria + non-functional
***Your Test Plan include several cases with sufficient some details but you can specify the inputs to the test, for example, test #1, says enter a username and password: What values do I enter?

# Wireframe
connect pages 
## System Diagram
**Figure 1:** System diagram of my project
Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (main, login, website_data and proj_lib). Then, these codes connect with a database of csv files (data_transactions and login).
## Flow Diagrams
3: 1 easy, two medium

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
30 tasks: for all the steps: planing, testing, development, feedback implementation, design (5)
**Table 1:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development (criterias A, B and C). The target completion date and the time estimate for each task is also shown.

# Criterion C

***Here you basically copied some parts of the code related to the criteria. This is good but not sufficient.  You can improve this section by adding a technical description of some of your code to show knowledge.  Also, we want to read here your thinking and rational to solve the client's requirements. "The way I solve this requirements was..."

### Code

***Explain each part: you can improve this part by describing the code in more detail so that you can show your knowledge of computer programming and algorithms. At this point you are just mentioning what the code is intended to do without how it does it. An example of a description is Quiz033.
Why this code is good, why i chose it and how helps the client, gpt

## Sources
StackOverFlow.com
YouTube.com
kivy.org/doc/stable/

## Tools used in Unit 3
- Functions
- For/while loops
- Input Validation
- If statements
- Encryption
- OOP paradigm
- KivyMD Library
- Relational databases
- SQLite, ORM
- Others

# Criteria D: Functionality

### Video
https://drive.google.com/file/d/15uBFJJsWgiyDIDAHGMM9TPk85QTE450Q/view?usp=sharing

# APENDIX
## A: Notes from First meeting - 10th February 2023
My client and me reunited in a 10-minute meeting.
She wants a mood tracker app. 
Log in and register
Main page with a box asking what is your mood today?
You can only answer with one word: Sad, happy, anxious, excited. List of options, you click one.
Notes screen. Every adjective has a different folder in which she writes. She writes in the page she has the feeling.
Delete and add notes options.

## B: Success Criteria confirmation:
![Captura de pantalla 2023-03-09 220642](https://user-images.githubusercontent.com/89135778/224033801-0d357219-a87a-412b-9413-bb9108cb1e01.png)
