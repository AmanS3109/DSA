#include <iostream>
#include <vector>
using namespace std;

int callSum(vector<int> arr, int target){

    for (int i = 0; i < arr.size(); i++)
    {
        int left = arr[i];
        int right = arr.size() - 1;
        int sum = left + right;
        if (sum == target)
        {
            return 1;
            if (sum < target)
            {
                left++;
            }
            else{
                right--;
            }
            
        }
        
    }
    return 0;
    
}

int main(){
    vector<int> arr = {2, 3, 4, 5, 6, 7, 8, 11};
    int funCall = callSum(arr, 4);
    cout << funCall << endl;
    return 0;
}
