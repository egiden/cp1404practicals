"""
CP1404/CP5632 Practical
"""
import random

from ipywidgets.widgets.widget_tagsinput import NumbersInputBase

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    for i in range(number_of_quick_picks):
        numbers = generate_unique_integers(NUMBERS_PER_LINE, MIN_NUMBER, MAX_NUMBER)
        numbers.sort()  # sort the numbers in ascending order
        # convert the numbers to strings and pad them with whitespace on the left to fill a length of 2
        padded_numbers = [f"{number:2}" for number in numbers]
        print(" ".join(padded_numbers))  # join the padded numbers with a space in between and print the result


def generate_unique_integers(number_of_integers: int, lower_bound: int, upper_bound: int):
    """Create a list of unique, random integers between given bounds (inclusive)."""
    integers = []
    while len(integers) != number_of_integers:
        integer = random.randint(lower_bound, upper_bound)
        # Make sure appending integer to integers will not result in repeated values
        if integer not in integers:
            integers.append(integer)
    return integers


main()
