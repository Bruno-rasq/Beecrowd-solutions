#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
    int n, area;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> area;
        double raio = sqrt(area / (4 * 3.14));

        if (raio < 12){
            float valor = area * 0.09;
            cout << "vermelho = R$ " << fixed << setprecision(2) << valor << endl;
        }
        
        else if (raio >= 12 && raio <= 15){
            float valor = area * 0.07;
            cout << "azul = R$ " << fixed << setprecision(2) << valor << endl;
        }
        
        else if (raio > 15){
            float valor = area * 0.05;
            cout << "amarelo = R$ " << fixed << setprecision(2) << valor << endl;
        }
    }
    return 0;
}