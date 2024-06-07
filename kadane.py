# brute force
# TC: O(N^2)

from cmath import inf


def largestSum(nums):
    maxSum = -inf
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum

# nums = [4, -1, 2, 7, -3, 4]
# print(largestSum(nums))

# kadane's algorithm
# TC: O(N)

def kadanes(nums):
    maxSum = -inf
    curSum = 0
    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

nums = [4, 2, -3, 1]
print(kadanes(nums))