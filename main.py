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
    string = text.lower()
    count = 0
    counted_characerts = {}
    for character in string:
        count += 1
        counted_characerts[character] = count 
    return counted_characerts
    print(counted_characerts)




def get_book_text(path):
    with open(path) as f:
        return f.read()


main()


