

def firstMissing(arr):
    if 1 not in arr:
        return 1
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i] = 1
    for i in range(len(arr)):
        if abs(arr[i]) < len(arr):
            arr[abs(arr[i])] = -abs(arr[abs(arr[i])]) #val points to an idx that should become neg
    print(arr)
    for i in range(1, len(arr)):
        if arr[i] > 0:
            return i
    return len(arr) 
a = [1, 2, 0] #3
print(firstMissing(a))
a = [3, 4, -1, 1] #2
print(firstMissing(a))
a = [7, 8, 9, 11, 12] #1
print(firstMissing(a))
