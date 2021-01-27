from model import *


class DoorKeeper:
    # def give_options(self):
    #     """takes no arguments and returns nothing, just shows the menu options"""
    #     print("1: create account")
    #     print("2: log in")
    #     print("3: forgot password")
    #     print("4: show all usernames and passwords")

    def get_response(self):
        print("1: create account")
        print("2: log in")
        print("3: forgot password")
        print("4: show all usernames and passwords")
        response = input("what would you like to do? (1, 2, 3 or 4): ")
        return response

    def create_account(self):
        username = input("create a username: ")
        existing_username = self.check_username(username)
        if existing_username:
            print("username exists already")
        else:
            password = input("create a password: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email_address = input("Email: ")
            create_user_model(first_name, last_name, username, password, email_address)

    def check_username(self, given_username):
        """
        ***    given_username STRING user provides name
        ***    checks if username already exists in the db
        ***    allows user creation if it was not found
        ***    if this returns true, then the user cannot be created
        ***    if it returns false then the user can be created and info beyond username is requested
        ***    returns a list called result
        """
        result = check_username_model(given_username)
        return result

    def log_in(self):
        """takes in no arguments. returns username if username and password matches or returns false"""
        user_name = input("What is your username?: ")
        pass_word = input("What is your password?: ")
        results = check_password_match_model(user_name, pass_word)
        if results:
            if results[0][0] == user_name and results[0][1] == pass_word:
                # returning the user name so user can use their data in the main menu
                return user_name
        else:
            print("Your password or username is incorrect, please contact an administrator")
            return results

    def forgot_password(self):
        # TODO 1: Build out a forgot password solution
        """this is one of those deals where we gotta email the user with a temporary password"""
        print("better remember it then")

    def show_users(self):
        # TODO 2: remove this functionality at some point
        results = show_users_model()
        print(results)

        # entered_username = input("Username: \n")
        # entered_pw = input("Password: \n")
        # if entered_username == correct_username and entered_pw == correct_pw:
        #     print("You successfully logged in")
        # else:
        #     print("your username and/or password is incorrect")

