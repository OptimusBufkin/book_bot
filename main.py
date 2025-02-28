"""
Contains main book bot logic
"""

from stats import *
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_number_of_words(text)
    num_chars = count_number_of_characters(text)
    sort_chars = sort_character_dictionary(num_chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_chars:
        char_count = list(item.values())
        if char_count[0].isalpha():
            print(f"{char_count[0]}: {char_count[1]}")
    print("============= END ===============")


main()
