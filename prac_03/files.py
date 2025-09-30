"""
CP1404 - Practical
Various ways of to read files.
"""

# Question 1
name = input("Enter name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", 'r')
# Read name and strip all leading and trailing whitespace
# and all escape characters
name = in_file.readline().strip()
print(f"Hi {name}!")

# Question 3
with open("numbers.txt", 'r') as in_file:
    lines = in_file.readlines()
    first_number = int(lines[0])
    second_number = int(lines[1])
    print(f"Result: {first_number + second_number}")

# Question 4
with open("numbers.txt", 'r') as in_file:
    sum_of_numbers = 0
    for line in in_file:
        sum_of_numbers += int(line)
    print(f"Result: {sum_of_numbers}")
