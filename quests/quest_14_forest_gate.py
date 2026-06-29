# Quest 14 - The Forest Gate
password = input("Speak the password to enter the forest: ")
if password == "oak":
    print("The gate swings open. Welcome, traveller!")
elif password == "elm":
    print("That is an old password. You may enter, but update your token.")
else:
    print("Wrong password! The gate stays shut.")
