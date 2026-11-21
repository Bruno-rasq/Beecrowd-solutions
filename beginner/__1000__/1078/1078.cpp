#include <iostream>
using namespace std;

int main() {

    int n;
    cin >> n;

    for(size_t i = 1; i <= 10; i++){
        cout << i << " x " << n << " = " << (i * n) << "\n";
    }

    return 0;
}