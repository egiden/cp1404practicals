"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Answer to question 1
# A ValueError will occur when an invalid or incorrect value is used in a particular opertation

# Answer to question 2
# A ZeroDivisionError will occur when an attempt is made to divide an number by zero.

# Answer to question 3
# Yes, the code can be altered to avoid a ZeroDivisionError.