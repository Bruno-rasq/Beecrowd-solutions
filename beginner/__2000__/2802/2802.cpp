#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    unsigned long long n;
    cin >> n;

    unsigned long long segmentos = 1 + 
        (((n - 1) * n) / 2) + 
        ((n * (n - 1) * (n - 2) * (n - 3)) / 24);

    cout << fixed << setprecision(0) << segmentos << endl;

    return 0;
}