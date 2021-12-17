from itertools import permutations


def task2(n):
    result = sorted(''.join(i) for i in list(permutations(n)))
    if result[-1] == n:
        return ""
    return result

print(task2(input('Enter word')))




