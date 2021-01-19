from model import *
import datetime

# games logic

# create
def write_game_record_controller():
    game_title = input("what is the game called?: \n").lower()
    now = datetime.datetime.now()
    game_start = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    print(game_start)
    minutes_played = input("how long did you play for?: \n")
    game_finished = "pending"
    user = "xsist14"
    write_to_games_list_for_user(game_title, game_start,game_finished, minutes_played, user)

# read
def show_user_games_list():
    '''show all of a users games from the terminal'''
    your_games = []
    results = read_games_list_for_user()
    for game in results:
        game = str(game)
        game = game.replace("(", "")
        game = game.replace(")", "")
        game = game.replace("'", "")
        game = game.replace(",", "")
        your_games.append(game)
    return(your_games)

def show_user_game_controller(name_of_game):
    results = show_user_game_model(name_of_game)
    for column in results:
        print(column)

# update
'''under construction'''

# delete
def delete_game_record_controller():
    user = "xsist14"
    name = input("what is the game called?: \n").lower()
    delete_from_games_list_for_user(name, user)

def fetch_user_games_list():
    print("getting the games from db for a user")



#sessions logic