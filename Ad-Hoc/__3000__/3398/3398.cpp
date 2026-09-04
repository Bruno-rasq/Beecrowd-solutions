#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    float moeda, result;
    int quantidade;

    cin >> moeda >> quantidade;

    result = moeda * quantidade;

    cout << fixed << setprecision(2) << result << endl;
    return 0;
}
