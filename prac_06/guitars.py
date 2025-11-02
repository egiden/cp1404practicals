from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    # Populate guitars list with Guitar class instances
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print()
        name = input("Name: ")

    # Display all the guitars
    print()
    display_guitars(guitars)


def display_guitars(guitars: list[Guitar]):
    """Print a formatted list of the details of guitars from a list of Guitar instances."""
    max_name_length = max([len(guitar.name) for guitar in guitars])  # Calculate length of longest guitar name
    # Create a list of cost values where each is formatted with a comma separator and two decimal places
    # e.g. 3456.7 -> "3,456.70"
    formatted_costs = [f"{guitar.cost:1,.2f}" for guitar in guitars]
    # Calculate length of the longest element of formatted_costs
    max_formatted_cost_length = max([len(formatted_cost) for formatted_cost in formatted_costs])

    # Print each guitar's details
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        right_aligned_name = f"{guitar.name:>{max_name_length}}"
        right_aligned_formatted_cost = f"{formatted_costs[i]:>{max_formatted_cost_length}}"
        print(
            f"Guitar {i + 1}:  {right_aligned_name} ({guitar.year}), worth $ {right_aligned_formatted_cost}{vintage_string}")


main()
