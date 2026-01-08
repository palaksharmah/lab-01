users_db = {
    "admin": "password891",
    "alice": "secure789",
    "bob": "my_secret"
}
def login():
    print("----LOGGING IN USER-----")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username in users_db and users_db[username] == password:
        print(f"Login successful! Welcome, {username}.")
        return True
    else:
        print("Error: Invalid username or password.")
        return False

is_logged_in = login()

if is_logged_in:
    print("Directing to Dashboard...")