#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int d, va, vb;
    while(cin >> d >> va >> vb){
        if(va <= vb){
            cout << "impossivel\n";
            continue;
        }
        double t = (double)d / (double)(va - vb);
        cout << fixed << setprecision(2) << t << "\n";
    }
}