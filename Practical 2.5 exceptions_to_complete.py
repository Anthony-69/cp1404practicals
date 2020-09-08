"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        integer = int(input("Value: "))
    except ValueError:
        print("Value is not a valid number.")
        print("Please enter a valid integer.")
print("Valid result is:", result)