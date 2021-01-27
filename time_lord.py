from datetime import *
from model import *


class TimeLord:
    """This is the location of all the code for sessions"""
    def __init__(self):
        pass

    """lots of time tracking code going on in here"""
    def add_session_controller(self, user):
        game_title = input("what is the game called?: \n")
        now = datetime.now()
        response = input("type 'y' to stop tracking")
        if response:
            today = date.today()
            session_date = today.strftime("%m/%d/%y")
            later = datetime.now()
            time_elapsed = later - now
            time_elapsed = int(time_elapsed.total_seconds())
            add_session_model(game_title, time_elapsed, session_date, user)
            print(f"You have played {game_title} for {time_elapsed} seconds")
            """time_elapsed game_title"""
            total_time = read_game_model_for_sessions(user, game_title)
            total_time = list(total_time)
            total_time = int(total_time[0])
            new_time_total = int(total_time) + int(time_elapsed)
            update_games_model_for_sessions(game_title, new_time_total, user)
            # passing the game title, time elapsed user to the sessions db
            input("type 'y' to continue")

    def read_sessions_controller(self, user):
        session_data = read_sessions_model(user)
        print(session_data)
