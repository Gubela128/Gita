print("Task 1 starts from here")
'''
Task #1
'''

# Global variable
int_list = [10, 20, 30, 40]


# Function to add a number to the global int_list
def add_to_int_list(number):
    global int_list  # Declare the use of the global variable
    int_list.append(number)


# Example of using the function
number_to_add = 50
add_to_int_list(number_to_add)

# Print the updated int_list
print(int_list)


print("\n")
print("Task 2 starts from here")
'''
Task #2
'''


def calculate_sum(number_list):
    # Use the built-in sum function to calculate the sum of the numbers
    total_sum = sum(number_list)
    return total_sum


# Example of using the function with the given list
numbers_to_sum = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
result_sum = calculate_sum(numbers_to_sum)

# Print the result
print("Sum of the numbers:", result_sum)


print("\n")
print("Task 3 starts from here")
'''
Task #3
'''

# Global variable
gl_str = "Global"


# Function that creates a local variable with the same name as the global variable
def create_local_variable():
    # Create a local variable with the same name as the global variable
    gl_str = "Local"
    return gl_str


# Call the function
local_variable_value = create_local_variable()

# Print the value of the local variable
print("Value of local variable:", local_variable_value)

# Print the value of the global variable outside the function
print("Value of global variable:", gl_str)


print("\n")
print("Task 4 starts from here")
'''
Task #4
'''


def sum_of_digits(number):
    # Base case: if the number is a single digit, return the number itself
    if number < 10:
        return number
    else:
        # Recursive case: add the last digit to the sum of the remaining digits
        return number % 10 + sum_of_digits(number // 10)


# Example of using the function
input_number = 12345
result_sum = sum_of_digits(input_number)

# Print the result
print("Sum of digits in", input_number, "is:", result_sum)


print("\n")
print("Task 5 starts from here")
'''
Task #5
'''


def reverse_string(input_str):
    # Base case: if the string is empty or has only one character, return the string itself
    if len(input_str) <= 1:
        return input_str
    else:
        # Recursive case: reverse the substring excluding the first character,
        # and append the first character at the end
        return input_str[-1] + reverse_string(input_str[:-1])


# Example of using the function
input_string = "Hello"
result_reverse = reverse_string(input_string)

# Print the result
print("Reverse of", input_string, "is:", result_reverse)