from os import system, name 

from model import *
from login import *
from controller import *
from art import logo
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def main_menu():
    clear()
    print(logo)
    print("1: add to game list")
    print("2: view games")
    print("3: delete game from list")
    print("4: add game session")
    print("5: delete game session")
    print("9: quit application")
    response = input("choose(1 2 3 4 5 or 9) \n")
    #add to game list
    if response == "1":
        create_game_record()
        main_menu()
    elif response == "2":
        view_all_games()
        response = input("type 'y' to continue")
        if response == 'y':
            main_menu()
    elif response == "3":
        delete_game_record_controller()
        main_menu()
    elif response == "4":
        print("feature under construction")
    elif response == "5":
        print("feature under construction")
    else:
        quit()

def create_game_record():
    write_game_record_controller()

def view_all_games():
    clear()
    your_games = show_user_games_list()
    games = ""
    for game in your_games:
        print(game.title())


print("Welcome to Bloosh! What would you like to do?")
main_menu()

def view_single_game():
    print(f"you have played the {current_game} for {minutes_played} minutes")

#sessions logic
def create_game_session_record():
    game_title = input("what is the game called?: \n")
    minutes_played = input("how long did you play for?: \n")