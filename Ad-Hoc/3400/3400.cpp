#include <iostream>
using namespace std;

const long long MOD = 1000000007;

long long derangement(long long n){
    if(n == 0) return 1;
    if(n == 1) return 0;
    long long a = 1; // D(0)
    long long b = 0; // D(1)
    for(long long i = 2; i <= n; i++){
        long long c = ((i - 1) * ((a + b) % MOD)) % MOD;
        a = b;
        b = c;
    }
    return b;
}

int main () {
    int n;
    cin >> n;
    cout << derangement(n) << "\n";
}