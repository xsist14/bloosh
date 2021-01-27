import sqlite3


# create
def write_to_games_list_for_user(name, date_started, date_finished, seconds_played, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO games VALUES(?,?,?,?,?)", (name, date_started, date_finished, seconds_played, user))
    connection.commit()
    connection.close()


def create_user_model(fname, lname, user, password, email):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",
                   (fname, lname, user, password, email))
    connection.commit()
    connection.close()


def add_session_model(game_name, seconds_played, session_date, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO sessions VALUES(?,?,?,?)",
                   (game_name, seconds_played, session_date, user))
    connection.commit()
    connection.close()


# read
def read_games_model(user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("select game_name, seconds_played from games where user = ?", (user,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


def read_game_model(game_title):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM games WHERE user = 'xsist14' and game_name=?", (game_title,))
    results = cursor.fetchone()
    connection.commit()
    connection.close()
    return results


def read_game_model_for_sessions(user, game_title):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT seconds_played FROM games WHERE user = ? and game_name=?", (user, game_title,))
    results = cursor.fetchone()
    connection.commit()
    connection.close()
    return results

def read_sessions_model(user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("select * from sessions where user = ?", (user,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


def show_users_model():
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


def check_username_model(username):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT user FROM users where user = ?", (username,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


def check_password_match_model(username, password):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT user, password FROM users where user=? and password =?", (username, password))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results

# TODO 14: Show all sessions
# TODO 15: add session time to overall game time for user also under an hour always displays less than an hour
# TODO 7: show all users function


# TODO 6: show single user function
# update
def update_game_record_model(game_title, game_start, game_finished, seconds_played, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute(''' UPDATE games
              SET date_started = ? ,
                  date_finished = ? ,
                  seconds_played = ?
              WHERE game_name = ?
              AND user = ?''', (game_start, game_finished, seconds_played, game_title, user,))
    connection.commit()
    connection.close()


def update_games_model_for_sessions(game_title, seconds_played, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute(''' UPDATE games
              SET seconds_played = ?
              WHERE game_name = ?
              AND user = ?''', (seconds_played, game_title, user,))
    connection.commit()
    connection.close()


# delete
def delete_from_games_list_for_user(name, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM games where game_name=(?) and user=(?)', (name, user,))
    connection.commit()
    connection.close()


def create_bloosh_database():
    """just leaving this code here in case I ever want to delete and recreate the database"""
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()

    command1 = """ CREATE TABLE IF NOT EXISTS
    games(game_name TEXT, date_started TEXT, date_finished TIMESTAMP, 
    seconds_played INTEGER, user TEXT)"""
    cursor.execute(command1)
    # speaking of deleting and recreating, I should change this to seconds played
    command2 = """ CREATE TABLE IF NOT EXISTS
    sessions(game_name TEXT, seconds_played INTEGER, session_date TEXT,
    user TEXT)"""
    cursor.execute(command2)

    command3 = """ CREATE TABLE IF NOT EXISTS
    users(first_name TEXT, last_name TEXT, user TEXT,
    password TEXT, email_address TEXT)"""
    cursor.execute(command3)

    connection.commit()
    connection.close()


# create_bloosh_database()
