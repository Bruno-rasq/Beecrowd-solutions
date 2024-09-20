#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    double circunferencia, r, PI = 3.14;
    cin >> r;

    circunferencia = 2 * (PI * r);

    cout << fixed << setprecision(2) << circunferencia << endl;
    return 0;
}