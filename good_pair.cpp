#include <iostream>
#include <vector>

int good_pair(std::vector<int>&nums){
    int n = nums.size();
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (nums[i] == nums[j]) {
                ans++;
            }
        }
    }
    return ans;
}
int main(){
    std::vector<int> nums = {1, 2, 3, 1, 1, 3};
    std::cout << good_pair(nums) << std::endl;  
    return 0;
}