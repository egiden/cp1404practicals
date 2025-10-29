from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []

    # Populate guitars list with Guitar class instances
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        print()

    # Display all the guitars
    print()
    print("These are my guitars:")
    max_name_length = max([len(guitar.name) for guitar in guitars])
    # Create a list of cost values where each is formatted with a comma separator and two decimal places
    # e.g. 3456.7 -> "3,456.70"
    formatted_costs = [f"{guitar.cost:1,.2f}" for guitar in guitars]
    max_formatted_cost_length = max([len(formatted_cost) for formatted_cost in formatted_costs])
    for i, guitar in enumerate(guitars):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        right_aligned_name = f"{guitar.name:>{max_name_length}}"
        right_aligned_formatted_cost = f"{formatted_costs[i]:>{max_formatted_cost_length}}"
        print(
            f"Guitar {i + 1}:  {right_aligned_name} ({guitar.year}), worth $ {right_aligned_formatted_cost}{vintage_string}")


main()
