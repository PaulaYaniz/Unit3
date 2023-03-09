# Imports
import sqlite3
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from p3_secure_password import encrypt_password, check_password
import datetime
import re
from kivymd.uix.progressbar import MDProgressBar

# Global variables for using username and emotion selected in different classes
my_username = ""
my_emotion = ""

# START: Database worker
class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()

# FIRST PAGE: What do you want to do next? Chose Login or Sign Up
class IntroScreen(MDScreen):
    # Pressing Login button gets you to the Login Screen
    def press_login(self):
        self.parent.current = "LoginScreen"

    # Pressing Sign up button gets you to Sign up Screen
    def press_signup(self):
        self.parent.current = "SignupScreen"

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

# Main Screen of the App: HomePage with options
class AppScreen(MDScreen):
    pass

# Feelings: How are you feeling today?
class Feelings(MDScreen):
    # Function for getting emotion selected on Kivy button
    def emotions(self, emotion):
        # Store emotion selected on global variable
        global my_emotion
        my_emotion = emotion
        # Write text on Notes Screen using emotion selected
        self.manager.get_screen("Notes").ids.notes_label.text = (f"Write here your feelings about being {emotion}")
        return emotion

    # Cancel operation and go back to the main AppScreen
    def cancel(self):
        self.parent.current = "AppScreen"

# Notes Page: Write about the emotion you selected
class Notes(MDScreen):
    # Create new note
    def new_note(self):
        # Get input from user and get current date with datetime library
        note = self.ids.note.text
        nowdate = datetime.datetime.now().date()
        # Add text written to database
        db = database_worker("p3_database.db")
        query = f"INSERT into notes (username, emotion, note, nowdate) values ('{my_username}', '{my_emotion}', '{note}','{nowdate}')"
        db.run_save(query)
        db.close()
        # Delete text written from widget so next time is blank and Change Screen
        self.ids.note.text = ""
        self.parent.current = "AppScreen"

    # Cancel operation and go back to the main page: AppScreen
    def cancel(self):
        self.ids.note.text = ""
        self.parent.current = "AppScreen"

# Folders: Read notes written organised by emotion
class Folders(MDScreen):
    # Get emotion selected
    def emotions(self, emotion):
        # Store emotion selected on global variable for later use
        global my_emotion
        my_emotion = emotion
        return emotion

    # Cancel operation: Go back to AppScreen
    def cancel(self):
        self.parent.current = "AppScreen"

# Read Notes according to emotion selected on previous page
class AllNotes(MDScreen):
    data_table = None
    # Get data from database
    def update(self):
        # Global variable to connect with emotion selected in class Folders
        global my_emotion
        emotion = my_emotion
        # Show text on label
        self.manager.get_screen("AllNotes").ids.table_label.text = (f"Your notes: {emotion}")
        # Get notes from database where the emotion is the one selected
        db = database_worker("p3_database.db")
        query = f"SELECT * FROM notes WHERE emotion='{my_emotion}' AND username='{my_username}'"
        data = db.search(query)
        db.close()
        self.data_table.update_row_data(None, data)

    # Delete a note selected with a checkbox
    def delete(self):
        rows_checked = self.data_table.get_row_checks()
        db = database_worker("p3_database.db")
        for r in rows_checked:
            id = r[0]
            query = f"delete from notes where id = {id}"
            print(query)
            db.run_save(query)
        db.close()
        self.update()

    # Cancel operation and go back to AppScreen
    def cancel(self):
        self.parent.current = "AppScreen"

    # Before the screen is shown, this code runs
    def on_pre_enter(self, *args):
        self.data_table = MDDataTable(
            size_hint = (.9, .7),
            pos_hint = {"center_x":.5, "center_y":.5},
            use_pagination = True,
            check = True,
            column_data = [("ID", 25), ("Username", 30), ("Emotion", 30),
                           ("Note",120), ("Date", 30)]
        )
        # add table and checkbox
        self.data_table.bind(on_check_press=self.check_pressed)
        self.add_widget(self.data_table)
        self.update()

    # Check row
    def check_pressed(self, table, current_row):
        print("a row was pressed ", current_row)

# Statistics: show basic data about user's well-being
class Statistics(MDScreen):
    # Count the number of time user has felt a negative feeling
    def count_bad(self):
        db = database_worker("p3_database.db")
        query = f"SELECT COUNT(emotion) FROM notes WHERE username='{my_username}' and (emotion='bored' or emotion='frustrated' or emotion='anxious' or emotion='sad' or emotion='angry');"
        data = db.search(query)
        # Show text on kivy saying the number
        self.manager.get_screen("Statistics").ids.count_bad.text = f"You have felt negative feelings {data[0][0]} times."
        db.close()
        return data[0][0]

    # Count the number of time user has felt a positive feeling
    def count_good(self):
        db = database_worker("p3_database.db")
        query = f"SELECT COUNT(emotion) FROM notes WHERE username='{my_username}' and (emotion='excited' or emotion='happy' or emotion='calm' or emotion='energetic' or emotion='confident');"
        data = db.search(query)
        # Show text on kivy saying the number
        self.manager.get_screen("Statistics").ids.count_good.text = f"You have felt positive feelings {data[0][0]} times."
        db.close()
        return data[0][0]

    # Count total amount of times the user has entered a feeling of any type
    def count_total(self):
        db = database_worker("p3_database.db")
        query = f"SELECT COUNT(emotion) FROM notes WHERE username='{my_username}';"
        data = db.search(query)
        # Show text on kivy saying the number
        self.manager.get_screen("Statistics").ids.count_total.text = f"Your total amount of notes written is {data[0][0]}"
        db.close()

        # Setting up the progress
        total = data[0][0]      # Total number for progress bar
        good_pct = self.count_good() / total     # Progress made (positive feelings)
        self.manager.get_screen("Statistics").ids.progress_bar.value = good_pct * 100

    # Show this when entering the page
    def on_enter(self):
        self.count_total()      # Total emotions felt
        self.count_good()       # Positive emotions felt
        self.count_bad()        # Negative emotions felt

        # Add progress bar
        self.progress_bar = MDProgressBar(max=100, value=0, size_hint=(0.8, None), height="20dp", pos_hint={"center_x": 0.5, "center_y": 0.3})
        self.manager.get_screen("Statistics").add_widget(self.progress_bar)

# Build the whole program
class project_unit3(MDApp):
    def build(self):
        return

# SQL queries for creating table users
query = """CREATE TABLE if not exists users(
        id integer primary key, 
        username text,
        email text,
        passwd text
        )"""

db = database_worker("p3_database.db")
db.run_save(query)
#db.close()

# SQL queries for creating table notes
query = """CREATE TABLE if not exists notes(
        id integer primary key, 
        username text,
        emotion text,
        note text,
        nowdate text
        )"""

#db = database_worker("p3_database.db")
db.run_save(query)
db.close()

test = project_unit3()
test.run()
