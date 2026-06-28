# Quest 22: The Personalized Scroll
# Concept: Functions with parameters - making functions flexible

def personalized_greeting(name, quest):
    """Prints a personalized greeting for an adventurer and their quest."""
    print(f"Hail, brave {name}! May your quest to {quest} be filled with glory!")

adventurer_name = input("What is your name, adventurer? ")
adventurer_quest = input("What is your quest? ")

personalized_greeting(adventurer_name, adventurer_quest)
