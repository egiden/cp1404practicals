for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
number_of_stars = int(input("Enter number of stars: "))
for i in range(0, number_of_stars):
    print('*', end='')
print()

# d
number_of_lines = int(input("Enter number of lines: "))
for i in range(1, number_of_lines + 1):
    for j in range(0, i):
        print('*', end='')
    print()