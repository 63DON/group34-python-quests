# Quest 18: The Loop of Riddles
secret_number = 42
print("I am thinking of a number between 1 and 100. Can you guess it?")
guess = None
while guess != secret_number:
    guess = int(input("Your guess: "))
    if guess == secret_number:
        print("Correct! You solved the riddle!")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
