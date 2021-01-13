from model import *
from login import *
from controller import *

current_game = "witcher 3"
minutes_played = 30
# your_games = [
#     "witcher 3",
#     "cyberpunk 2077",
#     "fall guys",
#     "spelunky 2",
#     "minecraft",
#     "forza horizon 4",
#     "sekiro"
# ]

your_games = []
def main_menu():
    response = input("Type 1 to add to game list, 2 to view all games, 3 to add session(incomplete), 4 to delete session(incomplete), 5 to delete game \n")
    if response == "1":
        create_game_record()
        main_menu()
    elif response == "2":
        view_all_games()
        main_menu()
    elif response == "3":
        print("feature under construction")
    elif response == "4":
        print("feature under construction")
    #delete game
    elif response == "5":
        delete_game_record_controller()
    else:
        quit()

def create_game_record():
    write_game_record_controller()

def view_all_games():
    show_user_games_list()

print("Welcome to Bloosh! What would you like to do?")
main_menu()

def view_single_game():
    print(f"you have played the {current_game} for {minutes_played} minutes")

def create_game_session_record():
    game_title = input("what is the game called?: \n")
    minutes_played = input("how long did you play for?: \n")