def insertion(list_a, length):
    for i in range(1, length):
        key = list_a[i]
        j = i - 1
        while j >= 0 and list_a[j] > key:
            list_a[j], list_a[j + 1] = list_a[j + 1], list_a[j]
            j = j - 1
        key = list_a[j + 1]
    return list_a


list = [5, 6, 3, 8, 9, 5, 2, 1, 5, 7, 8]
index = len(list)
print(insertion(list, index))



