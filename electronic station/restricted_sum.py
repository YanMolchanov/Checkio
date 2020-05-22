
def checkio(data):
    if len(data)==0: return 0
    return data[0]+checkio(data[1:])
