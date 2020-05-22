def is_all_upper(text: str) -> bool:
    alphas = [t for t in text if t.isalpha()]
    uppers = [t for t in text if t.isupper()]
    return  alphas == uppers and len(alphas) > 0


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
