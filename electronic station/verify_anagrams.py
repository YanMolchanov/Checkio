from string import ascii_letters

def verify_anagrams(first_word, second_word):
    symbs = lambda word: [s.lower() for s in word if s in ascii_letters]
    symbs1, symbs2 = symbs(first_word), symbs(second_word)
    return sorted(symbs1) == sorted(symbs2)


print(verify_anagrams("Programming", "Gram Ring Mop"))
print(verify_anagrams("Hello", "Ole Oh"))