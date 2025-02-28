"""
Contains main book bot logic
"""

from stats import get_book_text, count_number_of_words
def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_number_of_words(text)
    print(f"{num_words} words found in the document")


main()
