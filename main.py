def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)

    # Convert chars_dict to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in chars_dict.items()]

    # Sort the list
    char_list.sort(reverse=True, key=sort_on)

    # Print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

    print("--- End report ---")

def sort_on(dict_item):
    return dict_item["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
