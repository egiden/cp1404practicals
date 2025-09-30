"""
CP1404 - Practical
Various ways of to read files.
"""

# Question 1
name = input("Enter name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()
