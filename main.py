def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    counted_characters = get_count_character(text) 
    print(f"{num_words} words found in the document")
    print(counted_characters)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_character(text):
    counted_characerts = {}
    for character in text:
        lowered = character.lower()
        if lowered in counted_characerts:
            counted_characerts[lowered] += 1
        else:
            counted_characerts[lowered] = 1
    return counted_characerts

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


