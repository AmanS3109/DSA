#include <iostream>
using namespace std;


int raise(int base, int exp){
    if (exp == 0){
        return 1;
    }
    else{
        return base * raise(base, exp - 1);
    }
}
int main(){
    int result = raise(5, 0);
    cout << "the result is: " << result << endl;
    return 0;
}