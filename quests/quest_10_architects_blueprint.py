# Quest 10: The Architect's Blueprint
# Level 2 - Floating-Point Numbers
# Author: DON (63DON)
# Concept: Use float() so decimals are not lost when measuring.

print("The Architect needs the area of a rectangular room.")

# Ask the user for the length and width. They may be decimals,
# so we convert the input text into a float (a number with decimals).
length = float(input("Enter the length (in metres): "))
width = float(input("Enter the width (in metres): "))

# Area of a rectangle = length multiplied by width
area = length * width

# Print the result. round() keeps the output tidy to 2 decimal places.
print("The area of the room is", round(area, 2), "square metres.")
