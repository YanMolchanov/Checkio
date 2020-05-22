def time_converter(time):
    hr, mn = int(time.split(':')[0]), time.split(':')[1].split(' ')[0]
    hour = str(hr + 12 if 'p' in time and hr + 12 < 24 and int(mn) > 0 else 0 if 'a' in time and hr + 12 == 24 else hr)
    return f'0{hour}:{mn}' if len(hour) < 2 else f'{hour}:{mn}'
    
if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")