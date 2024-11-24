#include <iostream>
#include <iomanip>

using namespace std;

//logica correta mas ainda não resolve o problema.

int main(){

    int n
    cin >> n;

    long long segmentos = 1 + (((n - 1) * n) / 2) + ((n * (n - 1) * (n - 2) * (n - 3)) / 24);

    cout << fixed << setprecision(0) << segmentos << endl;

    return 0;
}