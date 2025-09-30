import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answer to question 1
# I saw a numbers between 5 and 20.
# The smallest number I could have seen is 5, and the largest 20.

# Answer to question 2
# I saw an odd numbers between 3 and 10.
# The smallest number I could have seen is 3, and the largest 9.
# Line 2 could not have produced a 4.

# Answer to question 3
# I saw numbers between 2.5 and 5.5
# The smallest number I could have seen is 2.5, and the largest 5.5.

# Produce random number between 1 and 100 (inclusive)
random_number = random.uniform(1, 100)
