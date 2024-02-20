import string

print("Task 1 starts from here")
'''
Task #1
'''

# Get user input
input_string = input("Enter a string: ")

print(input_string.encode('utf-8'))


print("\n")
print("Task 2 starts from here")
'''
Task #2
'''


input_string = input("Enter a string: ")

processed_string = input_string.strip().lower() + 'Python'

processed_string = processed_string.replace("python", "Python")

print(f"Processed string: {processed_string}")


print("\n")
print("Task 3 starts from here")
'''
Task #3
'''

# Get user input
input_string = input("Enter a string: ")

# Calculate the index to split the string
split_index = len(input_string) // 2

# Get the first half of the string
first_half = input_string[:split_index]

# Print the first half of the input string
print(f"The first half of the input string is: {first_half}")

print("\n")
print("Task 4 starts from here")
'''
Task #4
'''

input_string = input("Enter a string: ")

if any(char.isdigit() for char in input_string) and all(char in string.ascii_letters + string.digits for char in
                                                        input_string):
    print("The string is valid.")
else:
    print("The string is not valid.")


print("\n")
print("Task 5 starts from here")
'''
Task #5
'''
input_string = input("Enter a string: ")

bytes_value = input_string.encode('utf-8')
print(f"Bytes value: {bytes_value}")

decoded_string = bytes_value.decode('utf-8')
print(f"Decoded string: {decoded_string}")
