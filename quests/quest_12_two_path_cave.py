# Quest 12: The Two-Path Cave
# Concept: if-else statement - provides two possible paths

SECRET_PASSWORD = "dragon123"

user_input = input("Enter the password: ")

if user_input == SECRET_PASSWORD:
    print("Access Granted. Welcome, trusted ally!")
else:
    print("Access Denied. The gates remain sealed.")
