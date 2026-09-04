#include <iostream>
using namespace std;

int main() {
    int comprimento, largura, n_soldados;
    cin >> comprimento >> largura >> n_soldados;
    
    int hemisferioA = 0, hemisferioB = 0;
    double coeficiente = static_cast<double>(largura) / comprimento;  // Correção da divisão

    for (int i = 0; i < n_soldados; i++) {
        int x, y, p;
        cin >> x >> y >> p;
        if (y > coeficiente * x) {
            hemisferioA += p;
        } else {
            hemisferioB += p;
        }
    }
    
    cout << hemisferioA << " " << hemisferioB << endl;  // Simples e eficiente
}