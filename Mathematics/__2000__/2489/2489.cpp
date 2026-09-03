#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double A, D, R;
    while (cin >> A >> D >> R) {
        double rad = R * M_PI / 180.0;
        double H = A - D / tan(rad);

        cout << fixed << setprecision(4) << H << '\n';
    }
}