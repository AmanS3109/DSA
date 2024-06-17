# maximum size subarray sum equals to k

def equals_to_k(arr, k):
    sum = 0
    max_length = 0
    hashMap = {0: -1}
    
    for i, num in enumerate(arr):
        sum += num
        # If the difference (cumulative_sum - k) is found, update max_length
        if (sum - k) in hashMap:
            max_length = max(max_length, i - hashMap[sum - k])
        
        # Store the first occurrence of the cumulative sum
        if sum not in hashMap:
            hashMap[sum] = i
    
    return max_length

arr = [1, -1, 5, -2, 3]
k = 3
print(equals_to_k(arr, k))