def word_count(book):
    array_words = book.split()
    words = len(array_words)
    return words


def character_count(book):
    character_count = {}
    lower_case = book.lower()
    for char in lower_case:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def sorted_count(char_count):
    sorted_char = sorted(
        char_count.items(), key=lambda item: item[1], reverse=True
    )
    sorted_char = dict(sorted_char)
    return sorted_char
