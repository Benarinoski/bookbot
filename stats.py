# outputs entire book text as a string
# def get_book_text(book):
#    with open(book) as f:
#        file_contents = f.read()
#    return file_contents

def get_book_wc(book):
    word_count = 0
    with open(book) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            word_count += 1
    return word_count

def character_count(book):
    characters = {}
    with open(book) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        words = file_contents.split()
        for word in words:
            for char in word:
                if char not in characters:
                    characters[char] = 1
                else:
                    characters[char] += 1
    return characters

def letter_dict(characters):
    dict_list = []
    for chars in characters:
        char_dict = {}
        count = characters[chars]
        char_dict["char"] = chars
        char_dict["num"] = count
        dict_list.append(char_dict)
    return dict_list

def sorted_dict(dict):
    return dict["num"]

def main():
    word_count = get_book_wc("books/frankenstein.txt")
    characters = character_count("books/frankenstein.txt")
    character_dict = letter_dict(characters)
    character_dict.sort(reverse=True, key=sorted_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in character_dict:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")



main()