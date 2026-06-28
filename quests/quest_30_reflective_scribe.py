# Quest 30: The Reflective Scribe
# Level 6 - Grand Challenge
# Author: DON (63DON)
# Task: Revisit three earlier quests and add comments that explain
#       WHAT each part does and WHY. Below are three of my earlier
#       quests rewritten with detailed explanatory comments.

print("=== Reflective Scribe: three of DON's quests, fully commented ===\n")


# -------------------------------------------------------------------
# REVISITED QUEST 5: The Echoing Cave (reassigning variables)
# WHY: shows that a variable's value can change as events happen.
# -------------------------------------------------------------------
def revisit_quest_05():
    print("[Quest 5] The Echoing Cave")
    player_health = 100                       # WHAT: starting health. WHY: a baseline to change later.
    print("  Start health:", player_health)
    player_health = player_health - 25        # WHY: the monster's attack reduces health.
    print("  After troll attack:", player_health)
    player_health = player_health + 10        # WHY: the potion heals, adding to current value.
    print("  After potion:", player_health)
    print("  Final health:", player_health, "\n")


# -------------------------------------------------------------------
# REVISITED QUEST 20: The Even Number Forager (if inside a for loop)
# WHY: shows looping over a range and making a choice for each item.
# -------------------------------------------------------------------
def revisit_quest_20():
    print("[Quest 20] Even numbers from 1 to 20")
    for number in range(1, 21):               # WHAT: visit 1..20. WHY: range stops before 21.
        if number % 2 == 0:                   # WHY: % gives remainder; 0 means divisible by 2 (even).
            print("  ", number)
    print()


# -------------------------------------------------------------------
# REVISITED QUEST 29: The Code Breaker (loop + condition + break)
# WHY: shows limiting attempts and stopping early when the goal is met.
# -------------------------------------------------------------------
def revisit_quest_29(guess_list):
    print("[Quest 29] Code breaker (replaying guesses:", guess_list, ")")
    secret_code = 42                          # WHAT: the target. WHY: what every guess is compared to.
    won = False                               # WHY: remember if we succeeded after the loop ends.
    for attempt, guess in enumerate(guess_list, start=1):  # WHY: count attempts as we go.
        if guess == secret_code:
            print("   Attempt", attempt, "correct!")
            won = True
            break                             # WHY: no need to keep guessing once correct.
        else:
            print("   Attempt", attempt, "wrong.")
    if not won:
        print("   Never cracked it. Code was", secret_code)
    print()


# Run the three revisited quests so this file does something when executed.
# WHY: a script should demonstrate its functions, not just define them.
revisit_quest_05()
revisit_quest_20()
revisit_quest_29([10, 42, 99])   # sample guesses: second one is correct
