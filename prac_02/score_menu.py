"""
CP1404/CP5632 - Practical
Program to create interactive score menu
"""
from score import determine_score_status

MENU = """(G)et valid score (must be 0 - 100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
DEFAULT_SCORE = 0


def main():
    print(MENU)
    choice = input(">>> ").upper()
    score = DEFAULT_SCORE
    while choice != "Q":
        if choice == "G":
            new_score = int(input("Enter score\n>>> "))  # prompt user for score
            if is_valid_score(new_score):
                score = new_score
            else:
                print("Invalid score")
        elif choice == "P":
            result = determine_score_status(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you")


def print_stars(number_of_stars: int):
    """Print a string of asterisks of the given length."""
    print("*" * number_of_stars)


def is_valid_score(score: float) -> bool:
    """Check that the score is between 0 and 100 (inclusive)."""
    return 0 <= score <= 100


main()
