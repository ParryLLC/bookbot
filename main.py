import sys
from stats import get_book_text, word_count, characters_count, sort_characters_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    chars_count = characters_count(book_text)
    sorted_chars = sort_characters_count(chars_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()