from os import system, name 
from controller import *
from art import logo
from login import DoorKeeper

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

'''
new menu system
top layer is login, signup, forgot password
next layer is games, sessions, user info
games is crud
sessions is crud
user info can be random game quotes, statistics like most played
'''
door_keeper = DoorKeeper()
is_on = True
while is_on:
    door_keeper.give_options()
    response = door_keeper.get_response()
    if response == '1':
        door_keeper.create_account()
    elif response == '2':
        door_keeper.log_in()
    elif response == '3':
        door_keeper.forgot_password()
    elif response == '4':
        door_keeper.show_users()
    elif response == 'off':
        is_on = False




def login_screen():
    # TODO 10: need a full reboot on the menu system
    # TODO 11: make a logout function
    print()
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
# main_menu()

