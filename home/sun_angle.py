
def sun_angle(time):
    hr, mn = time[0:2], time[3:5]
    print(hr + mn)
    '''
    result =''
    x = float(time[0:2]+time[3:5])/100
    if x < 6 or x > 18:
        result = "I don't see the sun!"
    else:
        result = float((x - 6) * 15)
    return result
    '''
print(sun_angle("06:00"))


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert sun_angle("07:00") == 15
    #assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")