#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// converte graus para radianos
double rad(double graus){
    const double PI = 3.141592654;
    return graus * (PI / 180.0);
}

// utiliza a razão trigonométrica tg(ang) = cateto_oposto / ateto_adjacente.
int main() {
    double angulo, cateto_adj, altura_elfo;
    while(cin >> angulo >> cateto_adj >> altura_elfo){
        double r = rad(angulo);
        double cateto_oposto = cateto_adj * tan(r);
        double altura_arvore = cateto_oposto + altura_elfo;
        double tamanho_corda = 5 * altura_arvore;
        cout << fixed << setprecision(2) << tamanho_corda << "\n";
    }
}