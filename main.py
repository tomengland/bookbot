from stats import word_count, character_count, sorted_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def check_arguments():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    check_arguments()
    filepath = str(sys.argv[1])
    book = get_book_text(filepath)
    words = word_count(book)
    char_count = character_count(book)
    sorted_char_count = sorted_count(char_count)

    print(f"================== BOOKBOT ==================")
    print(f"Analyzing book found at {filepath}...")
    print(f"---------------- Word Count -----------------")
    print(f"Found {words} total words")
    print(f"---------------- Character Count ------------")
    for char, count in sorted_char_count.items():
        if char.isalpha():
            print(f"{char}: {count}")


main()
