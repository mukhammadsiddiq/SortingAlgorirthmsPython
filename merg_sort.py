def merg_sort(arr):
    if len(arr) > 1:
        right = arr[:len(arr) // 2]
        left = arr[len(arr) // 2:]

        merg_sort(right)
        merg_sort(left)

        i = 0 # ind for left array
        j = 0 # ind for right array
        k = 0 # ind for merged array

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


list = [5, 6, 7, 8, 4, 7, 9, 6, 3, 2, 7, 6, 8, 9, 0]
merg_sort(list)
print(list)

