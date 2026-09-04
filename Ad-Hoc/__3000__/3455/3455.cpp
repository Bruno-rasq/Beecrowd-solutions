#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main() {
    
    long long dinamica, grafica, geometrica;
    string tipo;
    double total = 0;
    
    cin >> grafica >> dinamica >> geometrica;
    cin >> tipo;
    
    if(tipo == "A"){
        total += grafica;
        total += dinamica * (3.0 / 2);
        total += geometrica * 2.5;
    }
    else if (tipo == "B"){
        total += dinamica;
        total += grafica * (2.0 / 3);
        total += geometrica * 2.5 * (2.0 / 3);
    }
    else if (tipo == "C"){
        total += geometrica;
        total += grafica * (1.0 / 2.5);
        total += dinamica * (3.0 / 2) * (1.0 / 2.5);
    }
    
    cout << static_cast<long long>(floor(total)) << endl;
    return 0;
}