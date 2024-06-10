def max_sum(arr):
    if len(arr) < 3:
        return None  # Or you could return float('-inf') if you prefer

    maximum = float('-inf')
    
    for i in range(len(arr) - 2):
        current_sum = arr[i] + arr[i + 1] + arr[i + 2]
        if current_sum > maximum:
            maximum = current_sum
            
    return maximum

print(max_sum([2, 3, 1, 9, 8, 4, 2]))