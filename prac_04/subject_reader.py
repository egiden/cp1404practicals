"""
CP1404/CP5632 Practical
Data file -> lists program
"""
from ftplib import all_errors
from multiprocessing.managers import all_methods

FILENAME = "subject_data.txt"


def main():
    all_subject_details = load_subject_details(FILENAME)
    display_all_subject_details(all_subject_details)


def load_subject_details(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    all_subject_details = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        all_subject_details.append(parts)
    input_file.close()
    return all_subject_details


def display_all_subject_details(data):
    """Print all subject details from a list containing lists of data formatted like: subject,lecturer,number of students."""
    for subject_details in data:
        subject_code = subject_details[0]
        lecturer = subject_details[1]
        number_of_students = subject_details[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")


main()
