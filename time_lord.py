from datetime import *
from model import add_session_model, read_sessions_model


class TimeLord:
    """This is the location of all the code for sessions4"""
    def __init__(self):
        print("step into my Tardis")

    """lots of time tracking code going on in here"""
    def add_session_controller(self, user):
        # TODO 16: put all this code in a method for class TimeLord
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
            # passing the game title, time elapsed user to the sessions db
            response = input("type 'y' to continue")

    def read_sessions_controller(self, user):
        session_data = read_sessions_model(user)
        print(session_data)
