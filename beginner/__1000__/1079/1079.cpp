#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int n;
    cin >> n;

    for(size_t i = 0; i < n; i++){
        double a, b, c;
        cin >> a >> b >> c;

        double avg = ((a * 2.0) + (b * 3.0) + (c * 5.0)) / 10.0;

        cout << fixed << setprecision(1) << avg << "\n";
    }

    return 0;
}