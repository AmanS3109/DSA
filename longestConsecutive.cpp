#include<bits/stdc++.h>
using namespace std;

int consecutiveSequence(int nums[], int m){
    unordered_set<int> numSet(nums.begin(), nums.end());
    int maxLength = 0;
    // Iterate through each number in the vector
    for (int num : nums) {
            // Check if this number is the start of a sequence
        if (numSet.find(num - 1) == numSet.end()) {
            int currentNum = num;
            int length = 1;

                // Count the length of the consecutive sequence
            while (numSet.find(currentNum + 1) != numSet.end()) {
                currentNum += 1;
                length += 1;
            }

                // Update the maximum length if the current sequence is longer
            maxLength = std::max(maxLength, length);
            }
        }

    return maxLength;

}
int main(){
    return 0;
}