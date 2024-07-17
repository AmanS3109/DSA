def sorted_squares(array):
    n = len(array)
    squared_array = [0] * n
    start = 0
    end = n - 1

    for index in range(n-1, -1, -1):
        smallerValue = array[start]
        largerValue = array[end]

        if abs(smallerValue) > abs(largerValue):
            squared_array[index] = smallerValue * smallerValue
            start += 1
        else:
            squared_array[index] = largerValue * largerValue
            end -= 1
    return squared_array

arr = [-4, -3, 2, 5, 9]
print(sorted_squares(arr))