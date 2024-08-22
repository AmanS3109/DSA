# acccepts two array, return true if 2nd array has squared values of 1st array

# naive solution  Time complexity: O(N^2)

def same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for num in arr1:
        if num ** 2 not in arr2:
            return False
    return True
    
arr1 = [1, 2, 3]
arr2 = [4, 1, 9]

#print(same(arr1, arr2))

# efficient solution TC:O(N)
def efficientSame(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    set2 = set(arr2)
    for num in arr1:
        if num ** 2 not in set2:
            return False
    return True
    
arr1 = [2, 2, 3]
arr2 = [4, 4, 9]

print(efficientSame(arr1, arr2))