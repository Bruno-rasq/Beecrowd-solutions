#include <iostream>

using namespace std;

int main() {

    long long n;
    cin >> n; 

    long long out = (n * (n - 3)) / 2;

    cout << out << endl;

    return 0;
}