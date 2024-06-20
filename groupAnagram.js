var groupAnagrams = function(strs) {
    // Initialize a map to store the grouped anagrams
    let map = new Map();

    // Iterate through each string in strs
    for (let s of strs) {
        // Create an array to count frequencies of each character
        let count = new Array(26).fill(0);

        // Count frequencies of characters in the current string
        for (let c of s) {
            count[c.charCodeAt(0) - 'a'.charCodeAt(0)]++;
        }

        // Convert the count array to a string representation
        let key = count.join('#');

        // If key does not exist in the map, create a new array
        if (!map.has(key)) {
            map.set(key, []);
        }

        // Add the current string to the array associated with the key
        map.get(key).push(s);
    }

    // Return all values from the map as an array of arrays
    return Array.from(map.values());
};
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))