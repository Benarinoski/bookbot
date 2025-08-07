import sys
from stats import get_book_wc
from stats import character_count
from stats import letter_dict
from stats import sorted_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_book_wc(sys.argv[-1])
    characters = character_count(sys.argv[-1])
    character_dict = letter_dict(characters)
    character_dict.sort(reverse=True, key=sorted_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at ...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in character_dict:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")



main()