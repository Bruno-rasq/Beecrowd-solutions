#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int tempo;
    while(cin >> tempo){
        if (tempo == 0) break;

        int ale = ceil(7.0 * tempo / 90);
        int bra = floor(tempo / 90.0);

        cout << "Brasil " + to_string(bra) + " x Alemanha " + to_string(ale) << endl;
    }
    return 0;
}