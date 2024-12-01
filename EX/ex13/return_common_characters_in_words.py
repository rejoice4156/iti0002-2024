"""Return unique characters in words."""


def common_characters_in_words(word1: str, word2: str) -> set:
    """
    Find common characters in two words.

    No loops required.

    common_characters_in_words("hello", "hi") => {"h"}
    common_characters_in_words("world", "low") => {"l", "o", "w"}
    """
    return set(word1).intersection(word2)


if __name__ == "main":
    # run this file to test the function
    print(common_characters_in_words("hello", "hi"))  # {"h"}
    print(common_characters_in_words("world", "low"))  # {"l", "o", "w"}
