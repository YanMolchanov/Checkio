import itertools.combinations

def combs(x):
    return [c for i in range(len(x)+1) for c in combinations(x,i)]


def bigger_together(ints):
    ints.sort()
    print(ints)
    los = list(map(str, ints))

    los.sort()
    print(los)
    los.sort(key=len)

    print(los)

    mydict = {}
    for i in range(len(max(los))):
        mydict[i+1] = [l for l in los if len(l) == i+1]
    print(mydict)
    for v in mydict.values():
        v.sort()
    print(mydict)

    #lolos = list(map(list, list(map(str, ints))))
    #print(lolos)

    '''
    for i in reversed(range(len(max(lolos)))):
        #lolos.sort(key=lambda x: len(x))
        lolos.sort(key=lambda x: x[i], reverse=True)
    print(lolos)
    '''


    '''
    lolos = list(map(list, list(map(str, ints))))
    
    lolos.sort(key=lambda x: len(x))
    lolos.sort(key=lambda x: x[-1])
    lolos.sort(key=lambda x: x[0])
    print(lolos)
    min = int(''.join(i for i in [item for sublist in lolos for item in sublist]))
    print(min)
    
    lolos.sort(key=lambda x: len(x), reverse=True)
    lolos.sort(key=lambda x: x[-1], reverse=True)
    lolos.sort(key=lambda x: x[0], reverse=True)
    print(lolos)
    max = int(''.join(i for i in [item for sublist in lolos for item in sublist]))
    print(max)
    return max - min
    '''
    '''
    ints.sort(key=str)
    min = int(''.join(str(i) for i in ints))
    ints.sort(key=str, reverse=True)
    max = int(''.join(str(i) for i in ints))
    print(min, max)
    return max - min
    '''

if __name__ == '__main__':
    print(combs([1, 420, 42, 423, 472, 4, 1, 111, 10, 157]))