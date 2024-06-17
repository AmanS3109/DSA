#include<bits/stdc++.h>
using namespace std;

bool squareRoot(int num){
    int a = sqrt(num);
    int a_sqr = a * a;
    if (a_sqr == num)
    {
        return true;
    }
    else{
        return false;
    }
    
}
int main(){
    int num = 14;
    cout << squareRoot(num) << endl;
    return 0;
}

