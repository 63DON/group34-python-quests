# Quest 20: The Even Number Forager
# Level 4 - Using if inside a for loop
# Author: DON (63DON)
# Concept: Loop through a sequence and make a decision about each item.

print("Foraging for even numbers between 1 and 20:")

# Loop over every number from 1 to 20 (range stops before 21)
for number in range(1, 21):
    # A number is even when dividing by 2 leaves no remainder (modulo 0)
    if number % 2 == 0:
        print(number, "is even")
