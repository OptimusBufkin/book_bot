"""
Helper functions for book bot
"""

def get_book_text(path: str) -> str:
    """
    Given *.txt file path, return file contents as a string.

    Args:
        path (str): Path to file.

    Returns:
        str: Contents of file.
    """
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")


def count_number_of_words(text: str) -> int:
    """
    Given string, count number of words in the string.

    Args:
        text (str): Input string.

    Returns:
        int: Number of words in input string.
    """
    text_list = text.split()
    return len(text_list)


def count_number_of_characters(text: str) -> dict:
    """
    Given string, count number of occurrences for each unique character.

    Args:
        text (str): Input string.

    Returns:
        dict: Dictionary of each unique character that appears in the input string
            with number of occurrences.
    """
    lower_text =  text.lower()
    num_char = {}
    for char in lower_text:
        if char not in num_char.keys():
            num_char[char] = 1
        else:
            num_char[char] += 1
    return num_char


def sort_character_dictionary(char_dict: dict) -> list:
    char_list = [{"character": x, "count": y} for x, y in char_dict.items()]
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def sort_on(dict):
    return dict["count"]