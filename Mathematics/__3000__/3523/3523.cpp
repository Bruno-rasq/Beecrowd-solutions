#include <iostream>
#include <cstdint>
using namespace std;

int main() {

    int64_t n, p, k;
    cin >> n >> p >> k;

    __int128 result = (__int128)p * k;

    cout << (result % n == 0 ? "SIM" : "NAO") << "\n";

    return 0;
}