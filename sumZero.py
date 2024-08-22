def sumToZero(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        summation = arr[left] + arr[right]
        if summation == 0:
            return [arr[left], arr[right]]
        elif summation > 0:
            right -= 1
        else:
            left += 1

arr = [-4, -3, -2, 0, 1, 2, 3]
print(sumToZero(arr))
    