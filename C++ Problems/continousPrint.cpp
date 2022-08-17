#include <iostream>
#include <cstdio>
using namespace std;

void printEnglish(int n) {
    if (n == 1) {
            cout << "one" << "\n"; 
    } else if (n == 2) {
            cout << "two" << "\n";
    } else if (n == 3) {
            cout << "three" << "\n";
    } else if (n == 4) {
            cout << "four" << "\n";
    } else if (n == 5) {
            cout << "five" << "\n";
    } else if (n == 6) {
            cout << "six" << "\n";
    } else if (n == 7) {
            cout << "seven" << "\n";
    } else if (n == 8) {
            cout << "eight" << "\n";
    } else if (n == 9) {
            cout << "nine" << "\n";
    } 
}

int main() {
    int a; 
    int b; 
    cin >> a >> b;
    for (int i = a; i <= b; i++) {
        if (i >= 1 && i <= 9) {
            printEnglish(i);
        } else if (i > 9 && i % 2 == 0) {
            cout << "even" << "\n";
        } else if (i > 9 && i % 2 == 1) {
            cout << "odd" << "\n";
        }
    }
    return 0;
}