
def maxPopulation(logs):
# Initialize a frequency array to store population changes
    freq = [0] * 2051
        
        # Iterate through each person's birth and death years
    for birth, death in logs:
        freq[birth] += 1  # Increment population for birth year
        freq[death] -= 1   # Decrement population for death year
        
        # Calculate prefix sum of the frequency array
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
        
        # Find the year with the maximum population
    max_population = max(freq)
        
        # Find the earliest year(s) with maximum population
    earliest_year = freq.index(max_population)
        
    return earliest_year

print(maxPopulation(logs=[[1993, 1999], [2000, 2010]]))
print(maxPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))