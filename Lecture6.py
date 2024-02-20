import re

print("Task 1 starts from here")
'''
Task #1
'''

my_list = []

while True:
    user_input = input("Enter a command (a {number}, r {number}, e): ").split()

    if not user_input:
        continue

    command = user_input[0]

    if command == 'a':
        try:
            number = int(user_input[1])
            my_list.append(number)
            print(f"Added {number} to the list. Current list: {my_list}")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number after 'a'.")

    elif command == 'r':
        try:
            number = int(user_input[1])
            my_list.remove(number)
            print(f"Removed {number} from the list. Current list: {my_list}")
        except (IndexError, ValueError):
            print("Invalid input. Please enter a valid number after 'r'.")

    elif command == 'e':
        print("Exiting the program.")
        break

    else:
        print("Invalid command. Please enter 'a {number}', 'r {number}', or 'e'.")

print("\n")
print("Task 2 starts from here")
'''
Task #2
'''

# Step a
my_list = [43, '22', 12, 66, 210, ["hi"]]
index_210 = my_list.index(210)
print(f"Index of 210: {index_210}")

# Step b
my_list[-1].append("hello")
print(f"List after adding 'hello': {my_list}")

# Step c
del my_list[2]
print(f"List after deleting element at index 2: {my_list}")

# Step d
my_list_2 = my_list.copy()
my_list_2.clear()

print(f"Original list: {my_list}")
print(f"Copied list cleared: {my_list_2}")

print("\n")
print("Task 3 starts from here")
'''
Task #3
'''


def validate_phone_number(phone_number):
    pattern = re.compile(r'\(\d{3}\) \d{3}-\d{3}')

    if pattern.fullmatch(phone_number):
        return f"Valid phone number: {phone_number}"
    else:
        return "Invalid format"


# Get user input
user_input = input("Enter a phone number in the format (123) 456-789: ")

# Validate and print result
result = validate_phone_number(user_input)
print(result)
