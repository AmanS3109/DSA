#include<bits/stdc++.h>
using namespace std;

int duplicates(vector<int> nums){
    int n = nums.size();
    if (n <= 2)
    {
        return n;
    }
    
    int left = 2;
    for(int right = 2; right < n; right++){
        if (nums[right] != nums[left - 2])
        {
            nums[left] = nums[right];
            left++;
        }
    }
    return left;
}
int main(){
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    cout << duplicates(nums) << endl;
}