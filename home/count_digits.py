import re

def count_digits(text: str) -> int:
    return len(re.findall('\d', text))


if __name__ == '__main__':
    count_digits('hi')
    count_digits('hi')
    count_digits('who is 1st here')
    count_digits('my numbers is 2')
    count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')
    count_digits('5 plus 6 is')
    count_digits('')

