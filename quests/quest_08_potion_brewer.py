# Quest 8: The Potion Brewer
dragon_scale_price = 10
elf_tear_price = 3
dragon_scales_needed = 3
elf_tears_needed = 5
cost_of_dragon_scales = dragon_scales_needed * dragon_scale_price
cost_of_elf_tears = elf_tears_needed * elf_tear_price
total_cost = cost_of_dragon_scales + cost_of_elf_tears
print(f"Dragon Scales: {dragon_scales_needed} x {dragon_scale_price} gold = {cost_of_dragon_scales} gold")
print(f"Elf Tears: {elf_tears_needed} x {elf_tear_price} gold = {cost_of_elf_tears} gold")
print(f"Total cost: {total_cost} gold")

cat > quests/quest_13_maze_of_many_choices.py << 'EOF'
# Quest 13: The Maze of Many Choices
score = int(input("Enter your score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Needs Improvement"
print(f"Your score: {score}/100  ->  Grade: {grade}")
