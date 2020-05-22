FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    h = (number // 100)
    st = (number % 100)
    t = st // 10
    s = (number % 10)
    hndr = FIRST_TEN[h - 1] + ' ' + HUNDRED + ' ' if h > 0 else ''
    ten = SECOND_TEN[s] if st > 0 and t == 1 else OTHER_TENS[t - 2] + ' ' if t > 0 else ''
    single = '' if s == 0 else FIRST_TEN[s - 1] if s > 0 and st < 10 or t > 1 else ''
    return f'{hndr}{ten}{single}'.strip()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')