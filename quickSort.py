import random
from random import randrange as rr


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(rr(len(array)))
        small = [i for i in array if i <= pivot]
        big = [i for i in array if i > pivot]
        return quicksort(small) + [pivot] + quicksort(big)


def randomInt(size, start, finish):
    array = []
    for i in range(size):
        rand_int = random.randint(start, finish)
        array.append(rand_int)
    return array


array = list(randomInt(20, 1, 40))
print(array)
result = quicksort(array)
print(result)
