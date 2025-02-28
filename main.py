"""
Contains main book bot logic
"""
import sys

from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_number_of_words(text)
    num_chars = count_number_of_characters(text)
    sort_chars = sort_character_dictionary(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_chars:
        char_count = list(item.values())
        if char_count[0].isalpha():
            print(f"{char_count[0]}: {char_count[1]}")
    print("============= END ===============")


main()
