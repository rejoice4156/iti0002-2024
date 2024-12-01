"""Organize by first symbols."""


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where the key is a character and the value is a list of words starting with this character.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting character and corresponding words in order of appearance.
    """
    new_dict = {}
    for word in strings:
        if len(word) > 0:  # Checking this makes sure word[0] exists and index is not out of range.
            letter = word[0]
            if letter not in new_dict:
                new_dict[letter] = []
            new_dict[letter].append(word)
    return new_dict


if __name__ == '__main__':
    print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))
    # => {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}
    print(organise_by_first_symbol([""]))  # => {}
    print(organise_by_first_symbol(["a", "ab", "abcd"]))  # => {'a': ["a", "ab", "abcd"]}
    print(organise_by_first_symbol(["a", "aDYh", "CtjK", "c", "Djyrc", "eBqa", "eJgLOLZU"]))
