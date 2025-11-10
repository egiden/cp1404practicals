"""
CP1404 Practicals
More Guitars
"""

from guitar import Guitar

FILE_NAME = 'guitars.csv'


def main():
    """Read guitar details from file, prompt user for more guitar details, save as Guitar objects, display."""
    # Create list of guitar objects
    guitars_from_file = load_guitars(FILE_NAME)
    guitars_from_user = get_guitars()
    all_guitars = guitars_from_file + guitars_from_user

    # Display all guitars
    all_guitars.sort()  # Sort guitars by year, oldest to newest
    print()
    display_guitars(all_guitars)

    # Write all guitars to file
    save_guitars(FILE_NAME, all_guitars)


def get_guitars() -> list[Guitar]:
    """Prompt user for guitar details and save as Guitar objects."""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print()
        name = input("Name: ")
    return guitars


def load_guitars(file_name: str) -> list[Guitar]:
    """Read file of guitar details and save as Guitar objects."""
    guitars = []
    in_file = open(file_name, 'r')
    # File format is like: Name,Year,Cost
    for line in in_file:
        parts = line.split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()
    return guitars


def save_guitars(file_name: str, guitars: list[Guitar]):
    """Write guitar details from list of Guitar objects to file."""
    # Save guitars
    out_file = open(file_name, 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()

    # Display completion message
    print()
    print(f"Guitars saved to {FILE_NAME}.")


def display_guitars(guitars: list[Guitar]):
    """Print guitar details from list of Guitar objects."""
    print("These are my guitars:")
    print()
    for guitar in guitars:
        print(guitar)


main()
