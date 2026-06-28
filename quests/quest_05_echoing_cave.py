# Quest 5: The Echoing Cave
# Level 1 - Reassigning Variables
# Author: DON (63DON)
# Concept: The value stored in a variable can be changed during the program.

# Start the player with full health
player_health = 100
print("Adventurer DON enters the Echoing Cave with full health:", player_health)

# A monster attacks! Subtract 25 from the current health.
player_health = player_health - 25
print("A cave troll strikes! You lose 25 health. Health is now:", player_health)

# The player finds a potion! Add 10 to the current health.
player_health = player_health + 10
print("You drink a glowing potion and recover 10 health. Health is now:", player_health)

# Show the final health after all the events
print("Final health after the cave:", player_health)
