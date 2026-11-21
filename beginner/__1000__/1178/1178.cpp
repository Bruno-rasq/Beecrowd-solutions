#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    double T;
    cin >> T;

    for(size_t idx = 0; idx < 100; idx++){
        cout << "N[" << idx << "] = ";
        cout << fixed << setprecision(4) << T << "\n";
        T /= 2.0;
    }
    
    return 0;
}