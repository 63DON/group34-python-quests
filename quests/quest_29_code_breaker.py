# Quest 29: The Code Breaker
# Level 6 - Grand Challenge
# Author: DON (63DON)
# Task: Give the user 3 attempts to guess the secret code (42).
#       Give feedback each guess, and stop on a correct guess
#       or after 3 failed attempts.

secret_code = 42          # the code the user must guess
max_attempts = 3          # how many tries they get
guessed_correctly = False # tracks whether they have won yet

print("Crack the vault! You have 3 attempts to guess the secret code.")

# Loop runs attempt 1, 2, 3
for attempt in range(1, max_attempts + 1):
    guess = int(input("Attempt " + str(attempt) + " - enter the code: "))

    if guess == secret_code:
        # Correct guess: celebrate and stop the loop early with break
        print("Correct! The vault clicks open. Well done, DON!")
        guessed_correctly = True
        break
    else:
        # Wrong guess: tell them how many attempts remain
        attempts_left = max_attempts - attempt
        print("Wrong code.", attempts_left, "attempt(s) left.")

# After the loop, if they never guessed right, reveal the answer
if not guessed_correctly:
    print("Out of attempts! The vault stays locked. The code was", secret_code)
