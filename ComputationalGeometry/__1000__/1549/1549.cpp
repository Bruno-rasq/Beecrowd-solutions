#include <iostream>
#include <numbers>   // std::numbers::pi (C++20)
#include <cmath>     // pow, cbrt
#include <iomanip>   // setprecision, fixed

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int pessoas, mililitros, b, B, H;
        cin >> pessoas >> mililitros >> b >> B >> H;

        float media = static_cast<float>(mililitros) / pessoas;
        float temp = cbrt((media * 3 * (B - b) / (numbers::pi * H)) + pow(b, 3));
        float h = media * 3 / (numbers::pi * (pow(temp, 2) + temp * b + pow(b, 2)));

        cout << fixed << setprecision(2) << h << endl;
    }

    return 0;
}