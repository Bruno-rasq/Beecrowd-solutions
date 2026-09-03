#include <bits/stdc++.h>
using namespace std;

string evenOrOdd(int n){
    if(n == 0) return "NULL\n";
    if(n % 2 == 0){
        if(n > 0) return "EVEN POSITIVE\n";
        return "EVEN NEGATIVE\n";
    }
    if(n > 0) return "ODD POSITIVE\n";
    return "ODD NEGATIVE\n";
}

int main() {
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        cout << evenOrOdd(n);
    }
}