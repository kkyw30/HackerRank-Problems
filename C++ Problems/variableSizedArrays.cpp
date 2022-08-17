#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n; 
    cin >> n; 
    int q; 
    cin >> q; 
    
    vector<vector<int>> arr(n);                // define array of arrays
    
    // fill up the arrays
    for (int i = 0; i < n; i++) {
        int num_elements;
        cin >> num_elements;
        arr[i].resize(num_elements);                      // make sure ith array in arr has length elements
        for (int j = 0; j < num_elements; j++) {
            cin >> arr[i][j];
        }
    }
    
    // get the queries
    for (int k = 0; k < q; k++) {
        int i, j; 
        cin >> i >> j; 
        cout << arr[i][j] << endl;                 // endl ends the line
    }
      
    return 0;
}