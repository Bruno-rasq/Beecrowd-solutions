#include <iostream>
using namespace std;

int GCD(int a, int b) {
    if (b == 0) return a;
    return GCD(b, a % b);
}

int main() {
    int x, y;
    cin >> x >> y;
    cout << GCD(x, y) << "\n";
    return 0;
}