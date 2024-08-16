# shortest word distance

# brute approach --> O(N^2)
# iterate through array n * n times
def minDistance(arr, word1, word2):
    #min_dist = float('inf')  # taking largest value to get minimum value
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == word1 and arr[j] == word2) or (arr[i] == word2 and arr[j] == word1):
                dist = abs(j-i)
                min_dist = min(min_dist, dist)
    return min_dist if min_dist != float('inf') else -1


#print(minDistance(arr, word1, word2))

# optimal solution --> 0(N)
# two pointer approach

def minDistance2(arr, word1, word2):
    i, j = -1, -1
    min_dist = float('inf')
    for k, word in enumerate(arr):
        if word == word1:
            i = k
        if word == word2:
            j = k
        if i != -1 and j != -1:
            dist = abs(i-j)
            min_dist = min(min_dist, dist)

    return min_dist
arr = ["practice", "makes", "practice", "coding", "makes"]
word1, word2 = "makes", "coding"
print(minDistance2(arr, word1, word2))