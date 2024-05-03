# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
# output : total numbers of pairs in the array.

def fun(x, nums):
    count = 0
    for i in range(0, x):
        if nums[i] == nums[x]:
            count += 1
    return count

def good_pair(nums):
    n = len(nums)
    ans = 0
    for x in range(0, n):
        ans += fun(x, nums)
    return ans

print(good_pair([1, 2, 1, 1, 3, 4]))