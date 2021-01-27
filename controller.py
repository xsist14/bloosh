from model import *
from datetime import *
import math
from time_lord import TimeLord

# games logic


# create
def add_game_controller(user):
    game_title = input("what is the game called?: \n").lower()
    now = datetime.now()
    game_start = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    print(game_start)
    minutes_played = 0
    game_finished = "pending"
    write_to_games_list_for_user(game_title, game_start, game_finished, minutes_played, user)




# read
def read_games_controller(user):
    """show all the user's games and times from the terminal"""
    your_games = []
    results = read_games_model(user)
    formatted_games = list(results)
    hour_text = ""
    for games in formatted_games:
        game_name = games[0]
        time_played = games[1]
        if time_played < 3600:
            time_played = "Less than an hour"
        elif time_played >= 3600:
            time_played = time_played / 3600
            time_played = int(math.floor(time_played))
            if time_played == 1:
                hour_text = " hour"
            else:
                hour_text = " hours"
        print(f"{game_name.title()}: {time_played}{hour_text} played")


def show_user_game_controller(name_of_game):
    results = read_game_model(name_of_game)
    for column in results:
        print(column)


def show_users_controller():
    all_users = show_users_model()
    print(all_users)


# update
def update_game_record_controller(user):
    game_title = input("what is the game called?: \n").lower()
    game_year_start = input("what year did you start playing?: \n").lower()
    game_month_start = input("what month did you start playing?: \n").lower()
    game_day_start = input("what day of the month did you start playing?: \n").lower()
    response = input("did you finish the game? type 'y' or 'n'")
    if response == "y":
        game_year_finish = input("what year did you finish playing?: \n").lower()
        game_month_finish = input("what month did you finish playing?: \n").lower()
        game_day_finish = input("what day of the month did you finish playing?: \n").lower()
        game_finished = game_year_finish + "-" + game_month_finish + "-" + game_day_finish
    else:
        game_finished = "pending"
    minutes_played = input("how long did you play for?: \n")
    game_start = game_year_start + "-" + game_month_start + "-" + game_day_start
    update_game_record_model(game_title, game_start, game_finished, minutes_played, user)


# delete
def delete_game_record_controller(user):
    name = input("what is the game called?: \n").lower()
    delete_from_games_list_for_user(name, user)

