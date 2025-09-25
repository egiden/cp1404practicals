"""A program that asks the user for a password, with error-checking and
repeats if the password doesn't meet a minimum length set by a variable."""


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password: str):
    """Print a string of asterisks equal in length to password."""
    print("*" * len(password))

def get_password(minimum_length=10) -> str:
    """Return a password from the user that meets a given minimum length.

    Keyword arguments:
        minimum_length -- the minimum length of the password (default 10)
    """
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Password must contain at least {minimum_length} characters.")
        password = input("Password: ")
    return password


main()
