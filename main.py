"""
Contains main book bot logic
"""

from stats import *
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_number_of_words(text)
    num_chars = count_number_of_characters(text)
    print(f"{num_words} words found in the document")
    print(f"Character count found in the document: {num_chars}")

main()
