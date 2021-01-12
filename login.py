correct_username = "jason@bloosh.com"
correct_pw = "password"

def logging_in():
    entered_username = input("Username: \n")
    entered_pw = input("Password: \n")
    if entered_username == correct_username and entered_pw == correct_pw:
        print("You successfully logged in")
    else:
        print("your username and/or password is incorrect")

