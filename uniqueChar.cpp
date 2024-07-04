#include<bits/stdc++.h>
using namespace std;

bool isUnique(string str){
    transform(str.begin(), str.end(), str.begin(), ::tolower);
    if (str.length() > 128){
        return false;
    }
    bool charSet[128] = {false};
    for (int i = 0; i < str.length(); i++)
    {
        int val = str[i];
        if (charSet[val])
        {
            return false;
        }
        charSet[val] = true;
    }
    return true;
}

int main(){
    string str = "Aman";
    bool ans = isUnique(str);
    cout << boolalpha << ans << endl;
    return 0;
}