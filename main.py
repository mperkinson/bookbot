import sys

from stats import get_character_count, get_word_count, sort_char_dict


def get_file_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def check_usage():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    check_usage()

    filepath = sys.argv[1]
    file_text = get_file_text(filepath)
    file_word_count = get_word_count(file_text)
    char_count = get_character_count(file_text)
    sorted_char_count = sort_char_dict(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {file_word_count} total words")
    print("--------- Character Count -------")
    for char_stat in sorted_char_count:
        if char_stat["char"].isalpha():
            print(f"{char_stat['char']}: {char_stat['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
