from collections import Counter


def task1():
    result = [input('Enter word: ') for i in range(int(input('enter numb: ')))]
    return Counter(result).values()

print(task1())
