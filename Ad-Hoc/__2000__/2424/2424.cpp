#include <iostream>
using namespace std;

int main(){
    int x, y;
    cin >> x >> y;

    bool resultado = x >= 0 && x <= 432 && y >= 0 && y <= 468;
    cout << (resultado ? "dentro" : "fora") << endl;
}