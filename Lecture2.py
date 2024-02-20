
"""
#1 task
"""

print("Task 1 starts here ")
# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check for division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Sort the numbers in ascending order
sorted_numbers = sorted([num1, num2])

# Print the results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Sorted Numbers: {sorted_numbers}")

print("\n")
""" 
#2 task
"""
print("Task 2 starts here ")
# Input the length of diagonals from the user
diagonal1 = float(input("Enter the length of the first diagonal: "))
diagonal2 = float(input("Enter the length of the second diagonal: "))

# Calculate the area of the rhombus
area = (diagonal1 * diagonal2) / 2

# Print the result
print(f"Area of the rhombus: {area}")

print("\n")
""" 
#3 task
"""
print("Task 3 starts here ")

# Input the number of meters from the user
meters = float(input("Enter the number of meters: "))

# Convert to other units
centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
miles = meters / 1609.34

# Print the results
print(f"Centimeters: {centimeters} cm")
print(f"Decimeters: {decimeters} dm")
print(f"Millimeters: {millimeters} mm")
print(f"Miles: {miles} miles")

print("\n")
""" 
#4 task
"""
print("Task 4 starts here ")

# Input the height and base from the user
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))

# Calculate the area of the triangle
area = 0.5 * base * height

# Print the result
print(f"Area of the triangle: {area}")