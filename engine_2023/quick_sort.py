def quick_sort(arr):
    if not arr: return []
    pivot = arr[0]
    left = []
    right = []
    for el in arr[1:]:
        if el < pivot:
            left.append(el)
        else:
            right.append(el)
    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [2, 1, 5, 3, 4]
print(quick_sort(arr))