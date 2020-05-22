def checkio(number):
    number_string = ''
    for n in range(9, 1, -1):
        while number > 0 and number % n == 0:
            number /= n
            number_string = str(n) + number_string
    if number > 1:
        return 0
    else:
        return int(number_string)
        
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd aexample"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
