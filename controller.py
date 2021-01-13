from model import *

#grabbing from the database
def fetch_user_games_list():
    print("getting the games from db for a user")

def write_game_record_controller():
    game_title = input("what is the game called?: \n")
    game_start = input("when did you start playing it?: \n")
    minutes_played = input("how long did you play for?: \n")
    game_finished = "pending"
    user = "xsist14"
    write_to_games_list_for_user(game_title, game_start,game_finished, minutes_played, user)
def delete_game_record_controller():
    user = "xsist14"
    name = input("what is the game called?: \n")
    delete_from_games_list_for_user(name, user)

#giving to the view
def show_user_games_list():
    results = read_games_list_for_user()
    print(results)
