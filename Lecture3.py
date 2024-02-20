"""
#1 task
"""

print("Task 1 starts here ")
# List of numbers
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

# Input a number from the user
user_number = int(input("Enter a number to check if it's in the list: "))

# Check if the number is in the list
if user_number in num_list:
    print(f"{user_number} is in the list.")
else:
    print(f"{user_number} is not in the list.")

print("\n")
""" 
#2 task
"""
print("Task 2 starts here ")
# Input a number from the user
user_number = int(input("Enter a number to check if it's even or odd: "))

# Check even or odd
if user_number % 2 == 0:
    print("Even")
else:
    print("Odd")


print("\n")
""" 
#3 task
"""
print("Task 3 starts here ")
# Create two string variables
st1 = input("insert first string: ")
st2 = input("insert second string: ")

# Compare the strings (ყოველთვის დაპრინტავს else conditionს რადგან სხვადასხვა ობიექტები იქნება)
if st1 is st2:
    print("Same object")
else:
    print("Different object")


print("\n")
""" 
#4 task
"""
print("Task 4 starts here ")

# List of numbers
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

# Input a number from the user
user_number = int(input("Enter a number: "))

# Check conditions
if num_list[2] < user_number < num_list[-1]:
    print("More than list elements")
elif user_number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")
