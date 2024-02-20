print("Task 1 starts from here")
'''
Task #1
'''


def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


# Example: Print the first 10 Fibonacci numbers
n = 10
result = fibonacci_sequence(n)
print(f"The first {n} Fibonacci numbers are: {result}")

print("\n")
print("Task 2 starts from here")
'''
Task #2
'''


def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters in both strings are equal
    return sorted(str1) == sorted(str2)


# Example: Check if "race" and "care" are anagrams
word1 = "race"
word2 = "care"

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")

print("\n")
print("Task 3 starts from here")
'''
Task #3
'''


def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Example: Calculate the factorial of 5
n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")

print("\n")
print("Task 4 starts from here")
'''
Task #4
'''


def count_char_occurrences(input_string, char_to_count):
    count = 0
    for char in input_string:
        if char == char_to_count:
            count += 1
    return count


# Example: Count the occurrences of 'a' in the string 'banana'
input_str = 'banana'
char_to_find = 'a'
result = count_char_occurrences(input_str, char_to_find)
print(f"The character '{char_to_find}' appears {result} times in '{input_str}'.")
