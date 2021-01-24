import sqlite3


# create
def write_to_games_list_for_user(name, date_started, date_finished, minutes_played, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO games VALUES(?,?,?,?,?)", (name, date_started, date_finished, minutes_played, user))
    connection.commit()
    connection.close()


def create_user_model(fname, lname, user, password, email):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",
    (fname, lname, user, password, email))
    connection.commit()
    connection.close()

# read
def read_games_list_for_user():
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("select game_name from games where user = 'xsist14'")
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results


def show_user_game_model(name):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM games WHERE user = 'xsist14' and game_name=?", (name,))
    results = cursor.fetchone()
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
    cursor.execute("SELECT * FROM users where user=? and password =?", (username, password))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results
# TODO 7: show all users function


# TODO 6: show single user function
# update
def update_game_record_model(game_title, game_start,game_finished, minutes_played, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute(''' UPDATE games
              SET date_started = ? ,
                  date_finished = ? ,
                  minutes_played = ?
              WHERE game_name = ?
              AND user = ?''', (game_start,game_finished,minutes_played,game_title,user,))
    connection.commit()
    connection.close()


# delete
def delete_from_games_list_for_user(name, user):
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM games where game_name=(?) and user=(?)', (name,user,))
    connection.commit()
    connection.close()


def create_bloosh_database():
    """just leaving this code here in case I ever want to delete and recreate the database"""
    connection = sqlite3.connect('bloosh1.db')
    cursor = connection.cursor()

    command1 = """ CREATE TABLE IF NOT EXISTS
    games(game_name TEXT, date_started TEXT, date_finished TIMESTAMP, 
    minutes_played INTEGER, user TEXT)"""
    cursor.execute(command1)

    command2 = """ CREATE TABLE IF NOT EXISTS
    sessions(game_name TEXT, minutes_played INTEGER, session_date TEXT,
    user TEXT)"""
    cursor.execute(command2)

    command3 = """ CREATE TABLE IF NOT EXISTS
    users(first_name TEXT, last_name TEXT, user TEXT,
    password TEXT, email_address TEXT)"""
    cursor.execute(command3)

    connection.commit()
    connection.close()
# create_bloosh_database()



