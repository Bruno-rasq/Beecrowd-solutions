#include <iostream>
#include <iomanip>

using namespace std;

int mani(){

    double a, b;
    cin >> a >> b;

    double result = (
        ((1.0 + a / 100) * (1.0 + b / 100)) - 1.0
    ) * 100;

    cout << fixed << setprecision(6) << result << endl;

    return 0;
}