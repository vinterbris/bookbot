path = 'books/frankenstein.txt'

def main():
    text = get_book_text(path)
    number_of_words = get_number_of_words(text)
    chars_dict = get_chars_dict(text)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{number_of_words} words found in the document\n")

    print_how_many_alphas_were_found(chars_dict)
    print('--- End report ---')


def get_book_text(path):
    with open(path) as file:
        return file.read()
        

def get_number_of_words(text):
    return len(text.split())


def get_chars_dict(text):
    num_of_chars = {}

    for char in text.lower():
        if char not in num_of_chars:
            num_of_chars[char] = 1
        else:
            num_of_chars[char] += 1
    return num_of_chars


def sort_on(pair_char_amount):
    return pair_char_amount[1]


def print_how_many_alphas_were_found(chars_dict):
    list_from_dict = list(chars_dict.items())

    list_from_dict.sort(reverse=True, key=sort_on)
    for pair in list_from_dict:
        if pair[0].isalpha():
            print(f'The {pair[0]} character was found {pair[1]} times')


main()