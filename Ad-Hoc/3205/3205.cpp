#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while(T--){
        int r, e, c;
        cin >> r >> e >> c;
        int profitAdvertise = e - c;

        if (profitAdvertise > r) cout << "advertise\n";
        else if (profitAdvertise < r) cout << "do not advertise\n";
        else cout << "does not matter\n";
    }
}