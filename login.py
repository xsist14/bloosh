from model import *


class DoorKeeper:

    def give_options(self):
        print("1: create account")
        print("2: log in")
        print("3: forgot password")
        print("4: show all usernames and passwords")

    def get_response(self):
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
        result = check_username_model(given_username)
        return result


    def log_in(self):
        user_name = input("What is your username?: ")
        pass_word = input("What is your password?: ")
        results = check_password_match_model(user_name, pass_word)
        print("no")

        print(results)
        print("results")

    def forgot_password(self):
        print("better remember it then")

    def show_users(self):
        results = show_users_model()
        print(results)

        # entered_username = input("Username: \n")
        # entered_pw = input("Password: \n")
        # if entered_username == correct_username and entered_pw == correct_pw:
        #     print("You successfully logged in")
        # else:
        #     print("your username and/or password is incorrect")

