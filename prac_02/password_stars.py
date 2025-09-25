"""A program that asks the user for a password, with error-checking and
repeats if the password doesn't meet a minimum length set by a variable."""
minimum_length = 10
password = input("Password: ")
while len(password) < minimum_length:
    print(f"Password must contain at least {minimum_length} characters.")
    password = input("Password: ")
print("*" * len(password))
