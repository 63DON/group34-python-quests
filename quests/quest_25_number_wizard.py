

secret_number = 7

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    if guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")
    guess = int(input("Guess again: "))

print("Correct! You found the secret number!")