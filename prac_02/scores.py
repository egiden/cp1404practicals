"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    # Get user score and print score status
    user_score = float(input("Enter score: "))
    user_score_status = determine_score_status(user_score)
    print(f"User score status: {user_score_status}")
    # Get random score and print score status
    random_score = random.randint(0, 100)
    random_score_status = determine_score_status(random_score)
    print(f"Random score: {random_score}")
    print(f"Random score status: {random_score_status}")


def determine_score_status(score: float) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
