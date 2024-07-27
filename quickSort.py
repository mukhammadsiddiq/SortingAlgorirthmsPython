import random
from random import randrange as rr


# Function definition for the quicksort algorithm
def quicksort(array):
    # Base case: if the array has less than 2 elements, it's already sorted
    if len(array) < 2:
        return array
    else:
        # Select a random pivot element from the array and remove it from the array
        pivot = array.pop(rr(len(array)))

        # Partition the array into two sub-arrays
        # 'small' will contain elements less than or equal to the pivot
        # 'big' will contain elements greater than the pivot
        small = [i for i in array if i <= pivot]
        big = [i for i in array if i > pivot]

        # Recursively apply quicksort to the partitions and combine the results
        return quicksort(small) + [pivot] + quicksort(big)


# Function to generate a list of random integers
def randomInt(size, start, finish):
    array = []
    # Generate 'size' random integers between 'start' and 'finish' (inclusive)
    for i in range(size):
        rand_int = random.randint(start, finish)
        array.append(rand_int)
    return array


array = list(randomInt(20, 1, 40))
print(array)
result = quicksort(array)
print(result)
