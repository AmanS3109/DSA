def reverseArray(array):
    left = 0
    right = len(array) - 1
    while left < right:
        # swap first element to the last from highest to lowest
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        left += 1
        right -= 1
    return array

arr = [1, 2, 3, 4, 5]
print(reverseArray(arr))
# TC: O(N)
# SC: O(1)