def rotateArray(array, k):
    n = len(array)
    k = k%n
    # reverse the whole array
    reverseArray(array, 0, n-1)
    #reverse till k
    reverseArray(array, 0, k-1)
    # reverse the rest
    reverseArray(array, k, n-1)
    return array
def reverseArray(array, left, right):
    while left < right:
        # swap first element to the last from highest to lowest
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        left += 1
        right -= 1
    return array

arr = [2, 3, 4, 5]
k = 2
print(rotateArray(arr, k))