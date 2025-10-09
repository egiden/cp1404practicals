"""
CP1404/CP5632 Practical
"""


def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
        numbers = []
        for i in range(5):
            number = int(input(f"Number: "))
            numbers.append(number)
        display_numbers_info(numbers)

    else:
        print("Access denied")


def display_numbers_info(numbers: list[int]):
    """Print information about numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


main()
