from datetime import datetime, timedelta

now = datetime.now()
session_time = now.strftime("%H:%M:%S")

# in-memory user list
user_list = [
    {"username": "admin", "password": "321", "attempts": 3, "blocked_until": None},
{"username": "ramon", "password": "123", "attempts": 3, "blocked_until": None}
]

# not logged in menu options
guest_options = {
    1: "Login",
    2: "Register",
    3: "Exit"
}

# menu options for logged users
logged_options = {
    1: "Rename Username",
    2: "Change Password",
    3: "Logout",
    4: "Exit"
}

# menu options for admin user
admin_options = {
    1: "Delete User",
    2: "Logout",
    3: "Exit"
}

# displays the user menu and returns the choice
def show_menu(options):
    while True:
        print("Welcome to the menu.\nOptions:")
        for key, value in options.items():
            print(f"{key} - {value}")

        action = input("Select an option: ")

        if action.isdigit():
            action = int(action)
            if action in options:
                return options[action]  # returns option value
        else:
            print("Invalid option. Try again.")

# validates username rules
def validate_username(user_list, username):
    if username != username.lower():
        print("Username must be all lowercase. Try again.")
        return False

    for user in user_list:
        if username == user["username"]:
            print("Username already taken. Try another one.")
            return False
    return True

#validate password rules
def validate_pass(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    elif password[0].islower():
        print("Password must start with an uppercase letter.")
        return False
    elif not any(c.isdigit() for c in password):
        print("Password must contain at least one number.")
        return False
    return True

#registers a new user
def register(user_list):
    while True: # username validation loop
        username = input("Create your username: ")
        if validate_username(user_list, username):
            break
    # username validated
    while True: # password validation loop
        password = input("Create a password: ")
        if validate_pass(password):
            user_list.append({
                "username": username,
                "password": password,
                "attempts": 3,
                "blocked_until": None
            })
            print(f"User {username} registered successfully.") # password validated
            break

# user login
def login(user_list):
    username = input("Enter your username: ")

    # searches for user in the user_list
    for user in user_list:
        if username == user["username"]:
            if user["blocked_until"] is not None: # checks if user is blocked
                if datetime.now() < user["blocked_until"]:
                    remaining = user["blocked_until"] - datetime.now()
                    print(
                        f"This user is temporarily blocked. "
                        f"Try again after {int(remaining.total_seconds())} seconds."
                    )
                    return None
                else: # unblocks the user when there is no remaining time
                    user["blocked_until"] = None
                    user["attempts"] = 3 # refresh login attempts
            # password attempts loop
            while user["attempts"] > 0:
                password = input("Enter your password: ")

                if password == user["password"]: # if its the same user password
                    print(f"You successfully logged as {username}.")
                    return user["username"]
                else:
                    user["attempts"] -= 1 # decreases login attempts
                    print(f"Incorrect password. Attempts left: {user['attempts']}.")
            user["blocked_until"] = datetime.now() + timedelta(minutes=3) # blocks user for 3 minutes
            print("You achieved 3 attempts. Try again after 3 minutes.")
            return None
    # executed if user was not found in the user_list
    print("This user does not exist.")
    return None

# logs out the current user
def logout(current_user):
    if current_user is not None:
        print("You successfully logged out.")
        return None

# renames a user (logged only)
def rename_user(user_list, old_username, new_username):
    for user in user_list:
        if user["username"] == old_username:
            user["username"] = new_username
            print(f"User {old_username} renamed to {new_username}.")
            return
    print("User not found.")

def change_pass(user_list, current_user):
    for user in user_list:
        if user["username"] == current_user:
            current_password = input("Enter your current password: ")

            if current_password != user["password"]:
                print("Password does not match. Try again.")
                return

            new_password = input("Enter new password: ")
            if not validate_pass(new_password):
                return

            user["password"] = new_password
            print(f"Password changed successfully.")
            return
    print("User not found.")

# deletes a user (admin only)
def delete_user(user_list, username):
    if username == "admin":
        print("User admin cannot be deleted.")
        return

    for user in user_list:
        if user["username"] == username:
            user_list.remove(user)
            print(f"User {username} deleted.")
            return

    print("User not found.")
# show all users
def show_users(user_list):
    print("USERS:")
    for user in user_list:
        print(user["username"])

# control variables
current_user = None
action = None

print(f"Session Time: {session_time}")

while True:
    if current_user is None:
        action = show_menu(guest_options)

        if action == "Login":
            current_user = login(user_list)

        elif action == "Register":
            register(user_list)

        elif action == "Exit":
            break

    elif current_user == "admin":
        action = show_menu(admin_options)

        if action == "Delete User":
            show_users(user_list)
            username = input("Select user to delete: ")
            delete_user(user_list, username)

        elif action == "Logout":
            logout()

        elif action == "Exit":
            break

    else:
        action = show_menu(logged_options)

        if action == "Rename Username":
            new_username = input("Enter your new username: ")
            rename_user(user_list, current_user, new_username)
            current_user = new_username

        elif action == "Change Password":
            change_pass(user_list, current_user)


        elif action == "Logout":
            current_user = logout()

        elif action == "Exit":
            break
