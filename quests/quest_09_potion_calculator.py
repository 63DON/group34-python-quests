# Quest 9 - The Potion Calculator
potions = int(input("How many potions do you have? "))
cost_each = float(input("How much does each potion cost? "))
total = potions * cost_each
print("Total cost:", total, "gold")
print("Average cost per potion:", total / potions, "gold")
