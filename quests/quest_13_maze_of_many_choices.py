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
