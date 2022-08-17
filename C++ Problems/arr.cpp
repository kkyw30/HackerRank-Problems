#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;   
    int arr[N];
    
    // fill up the values in the array
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    // print values in reverse order
    for (int i = N-1; i >= 0; i--) {
        cout << arr[i] << " ";
    }    
    
    return 0;
}
