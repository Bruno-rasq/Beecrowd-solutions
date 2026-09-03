#include <iostream>
#include <cstdint>
using namespace std;

int main(){
    int64_t n;
    while((cin >> n) && (n != 0)) {
        bool first = true;
        uint64_t square = 1;
        uint64_t odd = 3;
        while (square <= n) {
            if (!first) cout << ' ';
            cout << square;
            square += odd;
            odd += 2;
            first = false;
        }
        cout << '\n';
    }
}