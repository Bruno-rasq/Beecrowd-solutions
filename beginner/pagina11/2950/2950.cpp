#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    int distancia, diametro1, diametro2;
    cin >> distancia >> diametro1 >> diametro2;

    float resposta = static_cast<float>(distancia) / (diametro1 + diametro2);

    cout << fixed << setprecision(2) << resposta << endl;
    return 0;
}