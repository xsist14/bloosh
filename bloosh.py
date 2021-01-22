from os import system, name 
from controller import *
from art import logo


# TODO 5: make a function that shows all user names and passwords


# sessions logic


# define our clear function
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


def login_screen():
    clear()
    print("1: log in")
    print("2: sign up")
    print("3: forgot password")


'''
new menu system
top layer is login, signup, forgot password
next layer is games, sessions, user info
games is crud
sessions is crud
user info can be random game quotes, statistics like most played
'''


def main_menu():
    # TODO 10: need a full reboot on the menu system

    clear()
    print(logo)
    print("1: add to game list")
    print("2: view games")
    print("3: delete game from list")
    print("4: View Single Game Details")
    print("5: add game session")
    print("6: delete game Session")
    print("7: Update Game Record")
    print("9: quit application")

    response = input("choose(1 2 3 4 5 or 9) \n")
    # add to game list
    if response == "1":
        write_game_record_controller()
        main_menu()
    elif response == "2":
        show_games_controller()
        response = input("type 'y' to continue")
        if response == 'y':
            main_menu()
    elif response == "3":
        delete_game_record_controller()
        main_menu()
    elif response == "4":
        show_games_controller()
        name_of_game = input("Which game would you like to see from the list above?").lower()
        show_user_game_controller(name_of_game)
        response = input("type 'y' to continue")
        if response == 'y':
            main_menu()
    elif response == "5":
        show_games_controller()
        add_session_controller()
        print("add session under construction")
        # TODO 4: choose a game
        # TODO 2: write the time passing to the DB
        # TODO 3: add the time passed to the overall game
        main_menu()
    elif response == "6":
        print("delete session under construction")
        # TODO 9: add functionality to delete sessions
    elif response == "7":
        show_games_controller()
        update_game_record_controller()
        response = input("type 'y' to continue")
        if response == 'y':
            main_menu()
    else:
        quit()


show_users_controller()


print("Welcome to Bloosh! What would you like to do?")
main_menu()
