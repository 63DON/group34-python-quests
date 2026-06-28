# Quest 15: The Nested Riddle
# Level 3 - Nested if Statements
# Author: DON (63DON)
# Concept: An if statement inside another if for a second layer of decisions.

print("You reach a fork in the dungeon.")

# First decision: which direction?
direction = input("Do you go 'left' or 'right'? ").lower()

if direction == "left":
    # Only if they went left do we ask the next question (nested decision)
    action = input("You face an underground river. Do you 'swim' or 'wait'? ").lower()
    if action == "swim":
        print("You swim across and find a chest of glittering treasure! You win!")
    else:
        print("You wait too long, the tide rises, and you are swept back. Game over.")
else:
    # Any choice other than 'left' leads here
    print("You go right into a dead end and a sleeping dragon wakes up. Run!")
