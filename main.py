from stats import count_words
from stats import count_characters
from stats import sort_characters
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents




def main():
    file_path = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_count = count_words(get_book_text(file_path))
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_characters(get_book_text("books/frankenstein.txt"))
    print(sort_characters(character_count))
    print("============= END ===============")

main()
