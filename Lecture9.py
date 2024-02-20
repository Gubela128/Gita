from functools import reduce

print("Task 1 starts from here")
'''
Task #1
'''


def mint(list1, list2):
    # Use zip to create pairs from the two lists
    pairs = list(zip(list1, list2))
    return pairs


# Example of using the function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result = mint(list1, list2)

# Print the result
print(result)

print("\n")
print("Task 2 starts from here")
'''
Task #2
'''


def product_of_elements(lst):
    try:
        result = reduce(lambda x, y: x * y, lst)
        return result
    except TypeError:
        raise TypeError("Invalid parameter type. Please provide a list of numbers.")


# Example of using the function
input_list = [1, 2, 3, 4, 5]
try:
    output = product_of_elements(input_list)
    print("Output:", output)
except TypeError as e:
    print(e)

print("\n")
print("Task 3 starts from here")
'''
Task #3
'''

get_odd_elements = lambda lst: [x for x in lst if x % 2 != 0]

# Example of using the lambda function
input_list = [1, 2, 3, 4, 5, 6, 7]
result = get_odd_elements(input_list)

# Print the result
print(result)

print("\n")
print("Task 4 starts from here")
'''
Task #4
'''


def mint(str_list, ending):
    try:
        result = list(filter(lambda s: s.endswith(ending), str_list))
        return result
    except TypeError:
        raise TypeError("Invalid parameter type. Please provide a list of strings and a string (ending).")
    except Exception as e:
        raise e


# Example of using the function
input_strings = ['hello', 'world', 'coding', 'nod']
ending_str = 'ing'

try:
    output = mint(input_strings, ending_str)
    print("Output:", output)
except TypeError as e:
    print(e)
except Exception as e:
    print("An unexpected error occurred:", e)


