RomaNum = 'IVXLCDMivxlcdm'

def checkio(n):
    num = str(n)
    i = (len(num)-1)*2
    return Roma_structer(num, i)

def Roma_helper(n, i):
    RomaLogic = {0: '',
                 1: (RomaNum[i]*1),
                 2: (RomaNum[i]*2),
                 3: (RomaNum[i]*3),
                 4: (RomaNum[i]*1 + RomaNum[i + 1]*1),
                 5: (RomaNum[i + 1]*1),
                 6: (RomaNum[i + 1]*1 + RomaNum[i]*1),
                 7: (RomaNum[i + 1]*1 + RomaNum[i]*2),
                 8: (RomaNum[i + 1]*1 + RomaNum[i]*3),
                 9: (RomaNum[i]*1 + RomaNum[i + 2]),
                10: (RomaNum[i + 2])}
    return RomaLogic.get(n)

def Roma_structer(num, i):
    result = ''
    for n in range(len(num)):
        result = result + (Roma_helper(int(num[n]), i))
        if i < 0:
            break
        else:
            i -= 2
    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')