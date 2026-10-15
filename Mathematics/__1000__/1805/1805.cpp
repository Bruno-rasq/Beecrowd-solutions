#include <iostream>
using namespace std;
 
int main() {

    long long A,B;
    cin >> A >> B;
    long long soma = (A + B) * (B - A + 1) / 2;
    cout << soma << "\n";
 
    return 0;
}