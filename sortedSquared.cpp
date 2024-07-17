#include<bits/stdc++.h>
using namespace std;

vector<int> squaredArray(vector<int>& array){
    vector<int> squared;
    for (int num : array) {
        squared.push_back(num * num); // Calculate squares
    }

    std::sort(squared.begin(), squared.end()); // Sort squared values

    return squared;
}

int main() {
    std::vector<int> array = {-4, -1, 0, 3, 10}; // Example array
    std::vector<int> sortedSquare = squaredArray(array);

    for (int val : sortedSquare) {
        std::cout << val << " ";
    }
    // Output: 0 1 9 16 100

    return 0;
}