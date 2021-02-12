from os import system, name
from controller import *
from art import logo
from login import DoorKeeper
from time_lord import TimeLord
from tkinter import *

# sessions logic
window = Tk()
window.title("Bloosh")
window.config(padx=50, pady=50, bg="blue")


canvas = Canvas(width=1920, height=1080)

title_text = Label(text="bloosh", bg="blue", font=("Roboto", "24", "bold italic"), fg="white")
title_text.grid(row=0, column=0)

login_label = Label(text="Login", bg="blue", font=("Roboto", "24", "bold italic"), fg="white")
login_label.grid(row=1, column=1)

username_label = Label(text="Email:", bg="blue", font=("Roboto", "24", "bold italic"), fg="white")
username_label.grid(row=2, column=0)

user_entry = Entry(highlightthickness=0)
user_entry.grid(row=2, column=1)

password_label = Label(text="Password:", bg="blue", font=("Roboto", "24", "bold italic"), fg="white")
password_label.grid(row=3, column=0)

pass_entry = Entry(highlightthickness=0)
pass_entry.grid(row=3, column=1)

submit_button = Button(text="submit", bg="blue", font=("Roboto", "24", "bold italic"), fg="gray")
submit_button.grid(row=4, column=2)
window.mainloop()
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main_menu(user):
    # TODO 1: need a full reboot on the menu system
    """
    new menu system
    first layer is login, signup, forgot password doorkeeper
    second layer is games, sessions, logout
    third layer is inside games and sessions with an option to back out to the second layer
    games is crud
    sessions is crud
    maybe add random game quotes
    """
    # TODO 2: make a logout function
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
    print("8: View game sessions")
    print("9: quit application")
    print(f"Hello {user.title()}!")
    menu_response = input("choose(1 2 3 4 5 or 9) \n")
    # add to game list
    if menu_response == "1":
        add_game_controller(user)
        main_menu(user)
    elif menu_response == "2":
        read_games_controller(user)
        go_on = input("type 'y' to continue")
        if go_on == 'y':
            main_menu(user)
    elif menu_response == "3":
        delete_game_record_controller(user)
        main_menu(user)
    elif menu_response == "4":
        read_games_controller(user)
        name_of_game = input("Which game would you like to see from the list above?").lower()
        show_user_game_controller(name_of_game)
        go_on = input("type 'y' to continue")
        if go_on == 'y':
            main_menu(user)
    elif menu_response == "5":
        doctor = TimeLord()
        read_games_controller(user)
        doctor.add_session_controller(user)
        main_menu(user)
    elif menu_response == "6":
        print("delete session under construction")
        # TODO 3: add functionality to delete sessions
        # TODO 4: add classes for menu, sessions and games
        # TODO 5: Build out webapp with flask and deploy on a digital ocean droplet
    elif menu_response == "7":
        read_games_controller(user)
        update_game_record_controller(user)
        go_on = input("type 'y' to continue")
        if go_on == 'y':
            main_menu(user)
    elif menu_response == "8":
        doctor = TimeLord()
        doctor.read_sessions_controller(user)
        main_menu(user)
    else:
        quit()


door_keeper = DoorKeeper()
is_on = True
while is_on:
    response = door_keeper.get_response()
    if response == '1':
        door_keeper.create_account()
    elif response == '2':
        has_permission = door_keeper.log_in()
        if has_permission:
            user_name = has_permission
            main_menu(user_name)
    elif response == '3':
        door_keeper.forgot_password()
    elif response == '4':
        door_keeper.show_users()
    elif response == 'off':
        is_on = False

show_users_controller()


print("Welcome to Bloosh! What would you like to do?")
# main_menu()
