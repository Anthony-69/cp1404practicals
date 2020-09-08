"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    while numerator == 0:
        numerator = int(input("Enter the numerator: "))
    else:
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Q1. A ValueErrore will occur when the value given is not a number or has decimal places
# Q2. A ZeroDivisionError will occur when either numbers given are 0
# Q3. The could be changed to avoid a ZeroDivisionError by creating a loop that repeats until a user puts a number other than 0
# Changes made to code are shown above