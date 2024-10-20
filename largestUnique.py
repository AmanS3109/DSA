def largestunique(arr):
    largest = -1
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            if arr[i] > largest:
                largest = arr[i]
    return largest if largest != -1 else -1
    '''if largest != -1:
        return largest
    else:
        -1'''

arr = [5, 7, 3, 7, 5, 8]
print(largestunique(arr))