import sqlite3
#hi
# welcome to bloosh
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
users(first_name TEXT, last_name TEXT, user_name TEXT,
password TEXT, email_address TEXT)"""

cursor.execute(command3)
#seed data
# cursor.execute("INSERT INTO games VALUES ('Witcher 3','01-10-2021','01-11-2021', 20, 'xsist14')")
# cursor.execute("INSERT INTO games VALUES ('Assassins Creed Odyssey','01-10-2021','01-11-2021', 30, 'muddlefoot')")

cursor.execute("select * from games")
print(cursor.fetchone())

cursor.execute("select * from games where user = 'muddlefoot'")
print(cursor.fetchone())
connection.commit()

connection.close()