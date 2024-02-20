
print("Task 1 starts from here")
'''
Task #1
'''
n = int(input("insert number: "))
Sum = 0

print("Sum of all numbers from 1 to the inserted number is:", end=" ")

for i in range(n + 1):
    Sum += i
print(Sum)

print("\n")
print("Task 2 starts from here")
'''
Task #2
'''

n = int(input("insert number: "))

print("backward ordered numbers before inserted number:", end=" ")

while n > 0:
    if n != 1:
        print(n, end=",")
    else:
        print(n)
    n -= 1

print("\n")
print("Task 3 starts from here")
'''
Task #3
'''
Winner = 5
print("Let's Guess the number what I'm thinking of")
Guess = int(input("Guess the number: "))

while Guess != Winner:
    print("Try agian")
    Guess = int(input("Guess the number: "))
    if Guess == Winner:
        print("Good Job, You guessed the number correctly")

print("\n")
print("Task 4 starts from here")
'''
Task #4
'''

total_sum = 0
print("Program will print sum of positive numbers when you insert sum")
while True:
    user_input = input("Enter a number (type 'sum' to see the total): ")
    if user_input == 'sum':
        break
    number = float(user_input)
    if number > 0:
        total_sum += number
    else:
        print("Please enter a positive number.")

print(f"The sum of positive numbers entered is: {total_sum}")
