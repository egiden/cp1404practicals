from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # while True:
    #     name = input("Name: ")
    #     if name == "":
    #         break
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar = Guitar(name, year, cost)
    #     print(f"{guitar} added.")
    #     print()
    #     guitars.append(guitar)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        max_name_length = max([len(guitar.name) for guitar in guitars])
        max_cost_length = max([len(str(guitar.cost)) for guitar in guitars])
        formatted_name = f"{guitar.name:>{max_name_length}}"
        formatted_cost = f"{guitar.cost:>10,.{max_cost_length}}"
        print(f"Guitar {i + 1}: {formatted_name} ({guitar.year}), worth $ {formatted_cost}")


main()
