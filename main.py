from stats import count_words
from stats import count_characters
from stats import sort_characters
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(file_path))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_characters(get_book_text(file_path))
    print(sort_characters(character_count))
    print("============= END ===============")

main()
