"""
Word Occurrences
Estimate: 10 minutes
Actual:   23:34 minutes
"""


def main():
    text = input("Text: ")
    word_to_count = {}  # Contains key-value pairs of (word, no. word occurrence)
    # Add each word in text to word_to_count
    for word in text.split():
        # If the word is not yet in word_to_count, add it with an initial count of 1
        if word not in word_to_count:
            word_to_count[word] = 1
        # If the word is in word_to_count, increment its count by 1
        else:
            word_to_count[word] += 1
    length_of_longest_word = max([len(word) for word in word_to_count])
    sorted_keys = sorted(word_to_count)
    # Print each word and its count in alphabetical order, formatted like 'word : count' with the
    # 'word' section formatted to a width of the longest word in word_to_count
    for word in sorted_keys:
        print(f"{word:{length_of_longest_word}} : {word_to_count[word]}")


main()
