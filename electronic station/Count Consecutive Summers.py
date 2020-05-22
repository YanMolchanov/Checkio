def count_consecutive_summers(num):
    answer = 0
    for i in range(num):
        result = []
        for n in range(num)[i:]:
            result.append(n+1)
            if sum(result) == num:
                answer += 1
            elif sum(result) > num:
                break
    return answer

if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")