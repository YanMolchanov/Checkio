def cut_sentence(line, length):
    txt = line.split(" ")
    result = ''
    for t in txt:
        if len(result + t) <= length:
            result += t + ' '
            print(result)
        else:
            result = result.strip() + '...'
            break
    return result.strip()

if __name__ == '__main__':
    print(cut_sentence("Hi my name is Alex", 4))