#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long A, Y, F, P;
    cin >> A >> Y >> F >> P;

    if (A % Y == 0){
        cout << 0 << "\n";
    }
    else {
        long long days_forward = ((Y - A%Y)% Y) * F;
        long long days_backward = (A % Y) * P;

        cout << min(days_backward, days_forward) << "\n";
        return 0;
    }
}