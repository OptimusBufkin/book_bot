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
    with open(path) as f:
        return f.read()


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