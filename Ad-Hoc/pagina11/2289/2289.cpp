#include <iostream>
#include <bitset>

using namespace std;
typedef unsigned long long LONG;

int hammingDistance(LONG a, LONG b){
    LONG Xor = a ^ b;
    return bitset<64>(Xor).count();
}

int main(){

    LONG a, b;
    while (cin >> a >> b){
        if (a == 0 && b == 0) break;
        cout << hammingDistance(a, b) << endl;
    }
    return 0;
}