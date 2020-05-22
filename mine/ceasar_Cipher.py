
import string

def to_encrypt(text, delta):
    result = ''
    alphabet = (string.ascii_lowercase)
    for l in text:
        if l in alphabet:
            crypt = alphabet.index(l) + delta
            if crypt > 26:
                crypt = crypt - 26
            elif crypt < -26:
                crypt = crypt + 26
            result += (alphabet[crypt])
        else:
            result += l
    return result

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")