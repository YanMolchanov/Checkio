from collections import Counter

def frequency_sort(items):
    return sorted(items, key=lambda x: (Counter(items)[x], x), reverse=True)


if __name__ == '__main__':

    frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])
    frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])
    frequency_sort([17, 99, 42])
    frequency_sort([])
    frequency_sort([1])
