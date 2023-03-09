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

### Success criteria:
After meeting with the client ans sending her an email (See Appendix B), we agreed the following success criteria:
1. There is a secure registration and login system with requirements for password and email.
2. The application will contain a page asking how the client is feeling, to which the client will only be able to answer selecting one of the options given.
3. After selecting the feeling, the customer will be able to write notes about it.
4. The notes will be grouped in folders by the adjectives, and will have a date.
5. The application will allow the client to delete and add notes.
6. The application will give statistical information about the user's well-being: number of positive and negative emotions felt.

# Criteria B: Design
## Test Plan
| TEST                                              | DESCRIPTION                                                                  | PROCEDURE                                                                                                  | EXPECTED OUTPUT                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Unit testing of sign up page (functional)         | This test evaluates the sign up page.                                        | User tries to sign up, not following the password and email requirements. For example, password="password" | An error will be shown in red just below, explaining why it is incorrect. For example, password does not have digits and uppercase |
| Unit testing of new note (functional)             | This test is evaluating how the user add a new note into the notes database. | Click "How are ypu feeling" button, select an emotion, write about it.                                     | The note with the emotion will be saved on the database.                                                                           |
| Unit testing for buttons of feelings (functional) | Functionality of buttons related to emotions                                 | Click on each button and verify.                                                                           | The program will remember which button has just been pressed with a global variable.                                               |
| Unit testing buttons of folders (functional)      | Functionality of buttons related to folders of emotions.                     | Click on each button and verify.                                                                           | The program will lead the user to read the notes that have been written by her and have the tag of the emotion selected.           |
| Unit testing for deleting a note(functional)      | Check if the notes can be deleted from database                              | Select a note in Folders, Mark the checkbox, Click delete                                                  | Note will be deleted from database.                                                                                                |
| Unit testing for statistics (functional)          | Statistics appear in a text message in the user's screen.                    | Click the Statistics button                                                                                | Statistics will appear and they will change when users enter new data in the notes section.                                        |
| Quality of code review (non-functional)           | Use of comments, tabs, and developer-friendly files and variable names       | Check if the program is developer-friendly                                                                 | Program will have comments on every step of the code, and variable names are easy to understand.                                   |
| File organisation review (non-functional)         | Are all files organised? Folders, files, etc                                 | Check Pycharm folder and delete files that have not been used for the project.                             | On the project folder all files should have user-friendly names. All files are organised inside the folder.                        |
| Unit Test: Integration: whole login program       | Check whole code                                                             | Run the program and enter all inputs that a user would put.                                                | The program will not crash and will make its functions.                                                                            |

## System Diagram
![image](https://user-images.githubusercontent.com/89135778/224166933-f0d52d3b-e9b8-408a-a755-780d8bb3ef46.png)**Figure 1:** System diagram of my project
Fig.1 is the System Diagram. It shows the brand and type of the computer, with its specifications and the Operative System is has. The program runs in Python 3.8 and uses different codes (project_unit3.py, project_untit3.kv). Then, these codes connect with a database of sql files (p3_database.db).

# Wireframe
**Figure 2:**
![project_uni3](https://user-images.githubusercontent.com/89135778/224169767-c2b9007b-c950-4da1-a878-60bcfc992628.png)

Fig.2 is the Wirefram Diagram for the program.

## ER Diagrams
**Figure 3:**

![image](https://user-images.githubusercontent.com/89135778/224170770-25fceda6-ddcd-42a6-a891-3884c1891090.png)

Fig. 3 is the ER diagram for the database that my program uses.

## UML Diagrams
**Figure 4:**

![image](https://user-images.githubusercontent.com/89135778/224172941-c7bd1020-85dd-43a3-8e64-d04201208660.png)

Fig. 4 is the UML diagram for the classes of my program.

## Flow Diagrams
3: 1 easy, two medium

## Record of Tasks
| Task No |       Planned Action       |                               Planned Outcome                               | Time estimate | Target completion date | Criterion |
|:-------:|:--------------------------:|:---------------------------------------------------------------------------:|:-------------:|:----------------------:|:---------:|
|    1    |  First meeting with client |              Client described her requiremetns for the project              |     10min     |         Feb 10         |     A     |
|    2    | Second meeting with client |             Write Success Criteria and Client gives her agreeing            |     10min     |         Feb 20         |     A     |
|    3    |  Write the problem context |                              Problem definition                             |     10min     |         Feb 20         |     A     |
|    4    |   Write proposed solution  | Have a better understanding of what I have to do and write design statement |     15min     |         Feb 22         |     A     |
|    5    |      Create first page     |           Code first page, which contains login and singup buttons          |     45min     |         Feb 28         |     C     |
|    6    |     Create sign up page    |                          Code sign up and database                          |       1h      |         Feb 28         |     C     |
|    7    |     Create log in page     |                    Code log in and connect it to database                   |       1h      |         Feb 28         |     C     |
|    8    |       Make prototype       |                 Draw a digital protoype (Wireframe diagram)                 |       2h      |          Mar 1         |     B     |
| 9       | Third meeting with client  | Progress Check and show digital prototype                                   | 10min         | Mar 2                  | B         |
| 10      | Flowchart                  | Make flowchart diagrams                                                     | 1h            | Mar 5                  | B         |
| 11      | UML Diagram                | Draw UML Diagram                                                            | 20min         | Mar 5                  | B         |
| 12      | ER Diagram                 | Draw ER Diagram                                                             | 10min         | Mar 5                  | B         |
| 13      | Sign up requirements       | Add password and email requirements                                         | 40min         | Mar 6                  | C         |
| 14      | Make main page             | Code main page of the program, with 4 buttons                               | 30min         | Mar 6                  | C         |
| 15      | Make buttons feelings      | Code the feelings buttons and connect to database                           | 1h            | Mar 6                  | C         |
| 16      | Make folders buttons       | Code the folders buttons based on the the feelings buttons                  | 10min         | Mar 6                  | C         |
| 17      | Delete note                | Code how to delete a note                                                   | 10min         | Mar 6                  | C         |
| 18      | Cancel and back buttons    | Code cancel and back buttons to put everywhere around the program           | 15min         | Mar 6                  | C         |
| 19      | SQL check                  | Make changes on names of tables and columns so it is more user-friendly     | 15min         | Mar 7                  | C         |
| 20      | Database check             | Add username as a column of the notes table                                 | 10min         | Mar 7                  | C         |
| 21      | Design check               | Check kivy program and adjust design to make it more user-friendly          | 1h            | Mar 7                  | C         |
| 22      | Code review                | Make sure that there are comments everywhere                                | 30min         | Mar 7                  | C         |
| 23      | Make statistics            | Code statistics screen and add a progress bar                               | 1h            | Mar 7                  | C         |
| 24      | Test plan                  | Try tests and write on GitHub                                               | 30min         | Mar 7                  | B         |
| 25      | Code in GitHub             | Paste code on GitHub and explain it                                         | 1h            | Mar 8                  | C         |
| 26      | Sources                    | Get summary of all sources and put on repository                            | 10min         | Mar 9                  | C         |
| 27      | Tools used                 | Write tools used for unit 3                                                 | 5min          | Mar 9                  | C         |
| 28      | Check functionality        | Use the final app as a user, test it                                        | 30min         | Mar 9                  | D         |
| 29      | Video                      | Record video                                                                | 15min         | Mar 10                 | D         |


**Table 1:** Record of Task- showing the planning and working process of the project. All the steps are related to Planning, Solution Overview analysis and Development, and Functionality (criterias A, B C, and D). The target completion date and the time estimate for each task is also shown.

# Criterion C

***Here you basically copied some parts of the code related to the criteria. This is good but not sufficient.  You can improve this section by adding a technical description of some of your code to show knowledge.  Also, we want to read here your thinking and rational to solve the client's requirements. "The way I solve this requirements was..."Why this code is good, why i chose it and how helps the client, gpt


### Code
### Choose Login or Singup
```.py
# FIRST PAGE: What do you want to do next? Chose Login or Sign Up
class IntroScreen(MDScreen):
    # Pressing Login button gets you to the Login Screen
    def press_login(self):
        self.parent.current = "LoginScreen"

    # Pressing Sign up button gets you to Sign up Screen
    def press_signup(self):
        self.parent.current = "SignupScreen"
```
```.kv
<IntroScreen>
    size: 500, 500
    FitImage:
        source: "relaxing-wallpaper.jpg"

    MDCard:
        size_hint: 0.6, .7
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)

        MDBoxLayout:
            orientation: "vertical"
            MDLabel:
                text: "Welcome to YasModo, the best app to keep track of your feelings"
                font_style: "H3"
                font_name: 'Righteous-Regular'
                size_hint: .9, .5
                halign: "center"
                spacing: dp(1)

        MDBoxLayout:
            size_hint: 1, .8

            MDRaisedButton:
                id: login
                text: "[size=24][b]Login[/b][/size]"
                on_press: root.press_login()
                size_hint: .3, .6
                md_bg_color: "#eb86db"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: signup
                text: "[size=24][b]Sign up[/b][/size]"
                on_press: root.press_signup()
                size_hint: .3, .6
                md_bg_color: "#bfa1e3"
```
This code defines a screen called "IntroScreen" using the MDScreen class. This screen has two methods called "press_login" and "press_signup" that change the parent widget's current screen to either "LoginScreen" or "SignupScreen" when the corresponding button is pressed.
This is the first thing that user will see. It is also being made in kivy with Labels and Raised buttons, and with a user-friendly design.
![image](https://user-images.githubusercontent.com/89135778/224178231-ef66bd6d-4487-4b36-ae8c-4870b392ed2f.png)

### Log in
```.py
# LOG IN
class LoginScreen(MDScreen):
    # Log in option
    def try_login(self):
        # Change boolean for avoiding the page to change automatically after clicking next.
        change = True
        # Get user's input: username and password
        username = self.ids.username.text
        passwd = self.ids.passwd.text
        # Check existing usernames on database
        query = f"SELECT * from users WHERE username='{username}'"
        db = database_worker("p3_database.db")
        result = db.search(query=query)
        global my_username
        my_username = username
        db.close()

        # Idea -show visible password: https://www.youtube.com/watch?v=rIATjmj-Sb4&ab_channel=SBDeveloper

        # Match password and change screen
        if len(result) == 1:
            id, username, email, hashed = result[0]
            if check_password(user_password=passwd, hashed_password=hashed):
                self.parent.current = "AppScreen"
                # Delete text written
                self.ids.username.text = ""
                self.ids.passwd.text = ""

            # Incorrect password, show error message but do not change screen, stay there
            else:
                self.ids.passwd.error = True
                change = False
        # Incorrect username, show error message and delete both username and password written
        else:
            self.ids.username.error = True
            self.ids.username.text = ""
            self.ids.passwd.text = ""
            change = False

    # Cancel operation and go back to first page, IntroScreen
    def cancel(self):
        self.ids.username.text = ""
        self.ids.passwd.text = ""
        self.parent.current = "IntroScreen"
```
```.kv
<LoginScreen>
    size: 500, 500
    FitImage:
        source: "relaxing-wallpaper.jpg"

    MDCard:
        size_hint: 0.6, .7
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)

        MDLabel:
            text: "Login"
            font_style: "H3"
            font_name: 'Righteous-Regular'
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x":.5, "center_y":.5}

        MDTextField:
            id: username
            hint_text: "Enter your username"
            icon_left: "email"

            helper_text_mode: "on_error"
            helper_text: "Incorrect username"

        MDTextField:
            id: passwd
            hint_text: "Enter your password"
            icon_left: "key"
            password: True

            helper_text_mode: "on_error"
            helper_text: "Incorrect password"
        MDBoxLayout:
            size_hint: 1, .2

            MDRaisedButton:
                id: login
                text: "Login"
                on_press: root.try_login()
                size_hint: .3, 1
                md_bg_color: "#eb86db"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: cancel
                text: "Cancel"
                on_press: root.cancel()
                size_hint: .3, 1
                md_bg_color: "#bfa1e3"

```
This code defines a LoginScreen class with two methods. The try_login() method is responsible for checking the username and password provided by the user against the existing usernames and passwords in the database. If the username and password match, the method changes the screen to "AppScreen". If the password is incorrect, the method shows an error message but does not change the screen. If the username is incorrect, the method shows an error message and deletes both the username and password written. The cancel() method is responsible for deleting both the username and password written and changing the screen to "IntroScreen".
- try_login(): This method is triggered when the user tries to log in. It retrieves the user's input for their username and password, checks whether the username exists in the database, and then compares the hashed password with the entered password to determine whether they match. If the username and password are correct, the user is redirected to the main app screen. Otherwise, an error message is displayed.
- cancel(): This method is triggered when the user cancels the login operation. It resets the text fields and returns the user to the introductory screen.
The code connects with a database table named "users" with columns "id", "username", "email", and "hashed" and witht the check_password() function.
![image](https://user-images.githubusercontent.com/89135778/224178965-7b116e26-c906-4a74-968f-94d9e98919f1.png)

### Sign up
```.py
# SIGN UP
class SignupScreen(MDScreen):
    # Sign up option
    def try_signup(self):
        # Get user's input: username, email, password, and password verification
        username = self.ids.username.text
        email = self.ids.email.text
        passwd = self.ids.passwd_enter.text
        passwd_check = self.ids.passwd_check.text
        # Change boolean for avoiding the page to change automatically after clicking next
        change = True

        # Error if username is blank, but do not change screen
        if username == "":
            self.ids.username.error = True
            change = False

        # Email requirements. Code based in: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
        # Email needs to have a @ symbol, a . (point), and not other special characters.
        req_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        # If email is written incorrectly, show error message
        if not (re.fullmatch(req_email, email)):
            self.ids.email.error = True
            return
        if email == "":
            self.ids.email.error = True
            change = False

        # Password requirements. Code based in: https://stackoverflow.com/questions/41117733/validation-of-a-password-python
        # Password needs to have between 6 and 20 characters, have a number, a lowercase, and an uppercase at least
        req_passwd = re.compile('^(?=\S{6,20}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])')

        # If password is written incorrectly, show error message
        if not re.match(req_passwd, passwd):
            self.ids.passwd_enter.error = True
            return

        # Check that both passwords match
        if passwd != passwd_check:
            self.ids.passwd_check.error = True
            change = False

        # Check if username exists in the database
        db = database_worker("p3_database.db")
        query = f"SELECT * from users WHERE username ='{username}'"
        result = db.search(query=query)
        # If username exists, show error message
        if len(result) == 1:
            self.ids.username.error = True
            change = False

        # Check if email exists
        db = database_worker("p3_database.db")
        query = f"SELECT * from users WHERE email ='{email}'"
        result = db.search(query=query)
        # If email exists, show error message
        if len(result) == 1:
            self.ids.email.error = True
            change = False

        # passwords match, hash the password
        if change:
            hash = encrypt_password(passwd)
            db = database_worker("p3_database.db")
            query = f"INSERT into users (email, passwd, username) values('{email}','{hash}','{username}')"
            db.run_save(query)
            db.close()
            username = ""
            email = ""
            passwd = ""
            passwd_check = ""
            self.parent.current = "LoginScreen"

    # Cancel operation, delete text written, go back to first page, IntroScreen
    def cancel(self):
        self.ids.username.text = ""
        self.ids.email.text = ""
        self.ids.passwd_enter.text = ""
        self.ids.passwd_check.text = ""
        self.parent.current = "IntroScreen"
```
```.kv
<SignupScreen>
    size: 500, 500
    FitImage:
        source: "relaxing-wallpaper.jpg"

    MDCard:
        size_hint: 0.7, .8
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)

        MDLabel:
            text: "Sign up"
            font_style: "H3"
            font_name: 'Righteous-Regular'
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x":.5, "center_y":.5}

        MDTextField:
            id: username
            hint_text: "Enter username"
            icon_left: "account"
            size_hint: 1, .1

            helper_text_mode: "on_error"
            helper_text: "Username already exists or incorrect"

        MDTextField:
            id: email
            hint_text: "Enter email"
            icon_left: "email"
            size_hint: 1, .1

            helper_text_mode: "on_error"
            helper_text: "Email already exists or incorrect"

        MDTextField:
            id: passwd_enter
            hint_text: "Enter password"
            icon_left: "key"
            password: True
            size_hint: 1, .1

            helper_text_mode: "on_error"
            helper_text: "Password must have 6-20 characters, 1 upcase,  1 lowcase, and 1 digit"

        MDTextField:
            id: passwd_check
            size_hint: 1, .1
            hint_text: "Confirm password"
            icon_left: "key"
            password: True

            helper_text_mode: "on_error"
            helper_text: "Password does not match"

        MDBoxLayout:
            size_hint: 1, .15

            MDRaisedButton:
                id: signup
                text: "Submit"
                on_press: root.try_signup()
                size_hint: .3, 1
                md_bg_color: "#eb86db"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: signup
                text: "Cancel"
                on_press: root.cancel()
                size_hint: .3, 1
                md_bg_color: "#bfa1e3"
```
These functions are implementing the necessary validations for both login and signup processes and interact with the database to check for existing users, create new users, and store hashed passwords.
![image](https://user-images.githubusercontent.com/89135778/224179094-1eadf83f-14e5-4c01-bc96-0f7676d627a7.png)

## Sources
- StackOverFlow.com
- YouTube.com
- kivy.org/doc/stable/
- Chat GPT

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
