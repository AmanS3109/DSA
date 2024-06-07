# divide array in 2 subarray with equal sum

#optimized solution
def equal_sum(arr):
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False

    half_sum = total_sum // 2
    current_sum = 0

    for i in range(len(arr)):
        current_sum += arr[i]
        if current_sum == half_sum:
            return True
        elif current_sum > half_sum:
            return False
    return False

array = [3, 4, -2, 5, 8, 20, -10, 8]
print(equal_sum(array))   #TC: O(N)

# brute solution
def equal_sum(arr):
    for i in range(0, len(arr) - 1):
        sum1, sum2 = 0, 0
        for j in range(0, i + 1):
            sum1 += arr[j]
        for j in range(i + 1, len(arr)):
            sum2 += arr[j]        
        if sum1 == sum2:
            return True
        print(sum1, sum2)
    return False

array = [3, 4, -2, 5, 8, 20, -10, 8]
print(equal_sum(array)) #TC : O(N^2)