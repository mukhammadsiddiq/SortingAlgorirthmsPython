def selection_sort(array):      # defining function
    for i in range(0, len(array) - 1):      # outer loop will iterate throw the array length - 1
        min_ind = i
        for j in range(i + 1, len(array)):  # inner loop will iterate one index front
            if array[j] < array[min_ind]:   # condition will compare
                min_ind = j
        array[i], array[min_ind] = array[min_ind], array[i]     # swap


array = [5, 6, 3, 2, 7, 6, 5, 8, 9, 4]
selection_sort(array)
print(array)
