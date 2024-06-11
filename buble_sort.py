def buble_sort(list_a): # defining a function
    index = len(list_a) - 1 # getting length of the list using len()
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, index):
            if list_a[i] > list_a[i + 1]: # checking if first value is greater than
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i] # swap
    return list_a


print(buble_sort([4, 3, 1, 6, 3, 8, 9, 4, 2]))




