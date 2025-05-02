def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def word_count(book_text):
    words = book_text.split()
    return len(words)

def characters_count(book_text):
    char_count = {}
    
    for char in book_text:
        lowercase_char = char.lower()
        
        if lowercase_char in char_count:
            char_count[lowercase_char] += 1
        else:
            char_count[lowercase_char] = 1
    
    return char_count

def sort_characters_count(chars_count):
    sorted_chars = []

    for char, count in chars_count.items():
        char_list = {"char": char, "num": count}
        sorted_chars.append(char_list)

    def sort_on(dict):
        return dict["num"]

    sorted_chars.sort(key=sort_on, reverse=True)

    return sorted_chars   