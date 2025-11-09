"""
CP1404 Practicals
More Guitars
"""

from guitar import Guitar


def main():
    """Read file of guitar details, save as Guitar objects, display."""
    guitars = load_guitars('guitars.csv')
    guitars.sort()  # Sort guitars by year, oldest to newest
    display_guitars(guitars)


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


def display_guitars(guitars: list[Guitar]):
    """Display guitar details from list of Guitar objects."""
    for guitar in guitars:
        print(guitar)


main()
