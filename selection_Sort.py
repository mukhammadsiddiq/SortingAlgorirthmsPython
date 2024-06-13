def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_ind = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_ind]:
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]


array = [5, 6, 3, 2, 7, 6, 5, 8, 9, 4]
selection_sort(array)
print(array)
