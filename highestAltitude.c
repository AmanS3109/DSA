#include<stdio.h>

int largestAltitude(int* gain, int gainSize) {
    int max_alt = 0;
    int curr_alt = 0;
    for (int i = 0; i < gainSize; i++) {
        curr_alt += gain[i];
        if (curr_alt > max_alt) {
            max_alt = curr_alt;
        }
    }
    return max_alt;
}
int main(){
    int gain[] = {-5, 1, 5, 0, -7};
    int gainSize = sizeof(gain) / sizeof(gain[0]);
    int res = largestAltitude(gain, gainSize);
    printf("%d\n", res);
    return 0;
}