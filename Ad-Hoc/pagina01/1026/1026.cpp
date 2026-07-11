#include <bits/stdc++.h>
using namespace std;

int main(){
    uint64_t a, b;
    while(cin >> a >> b){
        int64_t c = a ^ b; // XOR
        cout << c << "\n";
    }
}