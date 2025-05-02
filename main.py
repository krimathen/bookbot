from stats import get_num_words
from stats import letter_count
from stats import data_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relative_path = sys.argv[1]
    book_text = get_book_text(relative_path)
    num_words = get_num_words(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    #print(letter_count(book_text))
    print("--------- Character Count -------")
    sorted_list = data_sort(letter_count(book_text))
    
    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    
    print("============= END ===============")

main()
