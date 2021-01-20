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

def login_screen():
    clear()
    print("1: log in")
    print("2: sign up")
    print("3: forgot password")


def main_menu():
    clear()
    print(logo)
    print("1: add to game list")
    print("2: view games")
    print("3: delete game from list")
    print("4: View Single Game Details")
    print("5: add game session")
    print("6: delete game Session")
    print("9: quit application")
    response = input("choose(1 2 3 4 5 or 9) \n")
    #add to game list
    if response == "1":
        write_game_record_controller()
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
        view_all_games()
        name_of_game = input("Which game would you like to see from the list above?").lower()
        show_user_game_controller(name_of_game)
        response = input("type 'y' to continue")
        if response == 'y':
            main_menu()
    elif response == "5":
        print("add session under construction")
    elif response == "6":
        print("delete session under construction")
    else:
        quit()



def view_all_games():
    clear()
    your_games = show_user_games_list()
    games = ""
    for game in your_games:
        print(game.title())


print("Welcome to Bloosh! What would you like to do?")
main_menu()



#sessions logic
def create_game_session_record():
    game_title = input("what is the game called?: \n")
    minutes_played = input("how long did you play for?: \n")