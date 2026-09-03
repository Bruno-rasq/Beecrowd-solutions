#include <iomanip>
#include <iostream>

using namespace std;

int main(){

    int hobbits, km;
    cin >> hobbits >> km;

    hobbits += 2;
    double result = static_cast<double>(km) / hobbits;

    cout << fixed << setprecision(2) << result << endl;

    return 0;
}