# sorting an array consists of 0s and 1s
def sort_zeros_ones(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
            
    return arr

arr = [0, 1, 1, 0, 1, 0, 1, 0]
sorted_arr = sort_zeros_ones(arr)
print("Sorted array:", sorted_arr)