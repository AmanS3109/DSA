#include<bits/stdc++.h>
#include<vector>
using namespace std;

int largestAltitude(vector<int>& gain){
    int max = 0;
    int curr_alt = 0;
    for (size_t i = 0; i < gain.size(); i++)
    {
        curr_alt += gain[i];
        if (curr_alt > max){
            max = curr_alt;
        }
    }
    return max;
}

int main(){
    vector<int> gain = {-5, 1, 5, 0, -7};
    int res = largestAltitude(gain);
    cout << res << endl;
    return 0;
}