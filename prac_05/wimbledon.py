"""
Emails
Estimate: 30 minutes
Actual:  46:43 minutes
"""

FILE_NAME = 'wimbledon.csv'


def main():
    champion_to_number_of_wins = {}
    countries = set()
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file.readlines()[1:]:
            if line.strip() != '':  # Skip empty lines
                line_data = line.split(',')
                champion_to_number_of_wins = process_champion_wins(champion_to_number_of_wins, line_data)
                # Update the countries set
                country = line_data[1]
                countries.add(country)

        print_wimbledon_data(champion_to_number_of_wins, countries)


def process_champion_wins(champion_to_number_of_wins: dict, line: list) -> dict:
    """Process the data in a list of strings about the Wimbledon gentlemen's singles champions,
    and extract information about the champion and their number of wins into a dictionary of
    key-value pairs of (champion name, no. wins).

    Parameters:
        champion_to_number_of_wins: The dictionary to update with the processed data.
        line: List of data to be processed. Must be formatted like so:
                    <year>, <country>, <champion>, <country>, <runner-up>
    """
    # Update champion_to_number_of_wins with the champion's name and the number of their wins
    champion = line[2]
    # Initiate the champion's number of wins to 1 if they are not in champion_to_number_of_wins
    if champion not in champion_to_number_of_wins:
        champion_to_number_of_wins[champion] = 1
    # Increment the champion's number of wins by 1 if they are in champion_to_number_of_wins
    else:
        champion_to_number_of_wins[champion] += 1
    # Return the updated dictionary
    return champion_to_number_of_wins


def print_wimbledon_data(champion_to_number_of_wins: dict, countries: set):
    """Print data about the Wimbledon gentlemen's singles champions, their names and number of wins,
    and their countries.
    """
    print("Wimbledon Champions:")
    for champion, number_of_wins in champion_to_number_of_wins.items():
        print(f"{champion} {number_of_wins}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(', '.join(sorted(countries)))


main()
