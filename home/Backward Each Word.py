def backward_string_by_word(text: str) -> str:
    rtext = ' '.join(list(reversed(text.split(' '))))
    return ''.join(list(reversed(rtext)))


if __name__ == '__main__':
    backward_string_by_word('')
    backward_string_by_word('')
    backward_string_by_word('world')
    backward_string_by_word('hello world')
    backward_string_by_word('hello   world')
    backward_string_by_word('welcome to a game')
