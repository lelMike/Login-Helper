import json
import pyperclip
import keyboard

options = ["0 - Show app names",
           "1 - Copy login details",
           "2 - Add new login",
           "3 - Change an existing login",
           "4 - Delete an existing login",
           "5 - Close"]

with open("logins.json") as f:
    logins = json.load(f)


def user_input_errorcheck(user_input, check_range):
    try:
        user_input = int(user_input)
    except:
        print("Wrong input, try again")
        return user_input_errorcheck(input(), check_range)
    if not user_input in range(check_range):
        print("Wrong input, try again")
        return user_input_errorcheck(input(), check_range)

    return user_input


def welcome_menu():
    print("Welcome to Login Helper! Type the instruction number you want to do.")
    for i in options:
        print(i)
    user_input = user_input_errorcheck(input(), len(options))
    if user_input == 0:
        return show_names()
    elif user_input == 1:
        return copy_login_details()
    elif user_input == 2:
        return add_new_login()
    elif user_input == 3:
        change_existing_login()
    elif user_input == 4:
        delete_existing_login()
    elif user_input == 5:
        print("Have a nice day, thank you for using the Login Helper!")
        return


def show_names():
    for _ in range(20):
        print(" ")
    print("To copy any app name, enter the app name number")
    print("All app names:")
    for ind, key in enumerate(logins.keys()):
        print(f"{ind} - {key}")
    print("\nTo return to the menu, enter any character")

    user_input = input()
    try:
        user_input = int(user_input)
    except:
        pass
    while type(user_input) == type(1):
        if int(user_input) in range(len(logins.keys())):
            pyperclip.copy(list(logins.keys())[user_input])
        else:
            for _ in range(20):
                print(" ")
            welcome_menu()
        user_input = input()
        try:
            user_input = int(user_input)
        except:
            pass
    for _ in range(20):
        print(" ")
    welcome_menu()


def copy_login_details():
    print("Enter the correct name of the app credentials you want to access")
    user_input = input()
    if not user_input.lower() in logins.keys():
        return copy_login_details()
    current_login = logins[user_input]
    print("Username copied to clipboard")
    pyperclip.copy(current_login[0])
    keyboard.wait("ctrl+v")
    print("password copied to clipboard")
    pyperclip.copy(current_login[1])
    keyboard.wait("ctrl+v")
    pyperclip.copy(" ")
    for _ in range(20):
        print(" ")
    welcome_menu()


def add_new_login():
    print("What should the app login name be?\n")
    new_app_name = input().lower()
    while new_app_name in logins.keys():
        print("There's already a name like this, try another one")
        new_app_name = input().lower()
    print("Alright, now copy the username\n")
    keyboard.wait("ctrl+c")
    new_username = pyperclip.paste()
    print("Got it! Now copy the password\n")
    keyboard.wait("ctrl+c")
    new_password = pyperclip.paste()

    logins[new_app_name] = [new_password, new_username]
    with open("logins.json", "w") as file:
        json.dump(logins, file)
    print("Successfully added login, press r to return to menu")
    keyboard.wait("r")
    for _ in range(20):
        print(" ")
    welcome_menu()


def change_existing_login():
    print("What login do you want to change?\n")
    change_login_name = input().lower()
    while change_login_name not in logins.keys():
        print("Login not found, try again")
        change_login_name = input().lower()
    curr_login_info = logins[change_login_name]
    print("Found it! What change do you want to make?")
    print("0 - Username\n1 - Password\n2 - Both")
    user_input = user_input_errorcheck(input(), 3)
    if user_input == 0:
        print("What should be the new username?")
        new_username = input()
        logins[change_login_name] = [new_username, logins[change_login_name][1]]
        with open("logins.json", "w") as file:
            json.dump(logins, file)
    elif user_input == 1:
        print("What should be the new password?")
        new_password = input()
        logins[change_login_name] = [logins[change_login_name][0], new_password]
        with open("logins.json", "w") as file:
            json.dump(logins, file)
    else:
        print("What should be the new username?")
        new_username = input()
        print("What should be the new password?")
        new_password = input()
        logins[change_login_name] = [new_username, new_password]
        with open("logins.json", "w") as file:
            json.dump(logins, file)
    print("Successfully changed login details, press r to return to menu")
    keyboard.wait("r")
    for _ in range(20):
        print(" ")
    welcome_menu()


def delete_existing_login():
    print("What login do you want to delete?")
    delete_login_name = input().lower()
    while delete_login_name not in logins.keys():
        print("Login not found, try again")
        delete_login_name = input().lower()
    logins.pop(delete_login_name)
    with open("logins.json", "w") as file:
        json.dump(logins, file)
    print("Successfully deleted login, press r to return to menu")
    keyboard.wait("r")
    for _ in range(20):
        print(" ")
    welcome_menu()


welcome_menu()