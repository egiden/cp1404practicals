"""
CP1404 Practical
Hexadecimal colours in a dictionary
"""

NAME_TO_CODE = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'AliceBlue': '#f0f8ff',
                'Alizarin crimson': '#e32636', 'Amaranth': '#e52b50', 'Amber': '#ffbf00', 'Amethyst': '#9966cc',
                'AntiqueWhite': '#faebd7', 'AntiqueWhite1': '#ffefdb', 'AntiqueWhite2': '#eedfcc'}

# Create an identical dictionary to NAME_TO_CODE where the keys are all in upper case
name_to_code_upper = {colour_name.upper(): code_name for colour_name, code_name in NAME_TO_CODE.items()}

colour_name = input("Enter colour name: ")
while colour_name != "":
    try:
        print(colour_name, "is", name_to_code_upper[colour_name.upper()])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ")
