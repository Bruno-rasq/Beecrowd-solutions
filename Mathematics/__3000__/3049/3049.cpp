
#include <iostream>
using namespace std;

int main() {
    int base_nota = 160; // cm
    int altura_nota = 60; // cm
    int area_total = base_nota * altura_nota;

    int B, T;
    cin >> B >> T;

    // Área do lado esquerdo: trapézio com bases B (base) e T (topo)
    float area_esquerda = ((float)(B + T) * altura_nota) / 2.0;

    // Área do lado direito é o restante da nota
    float area_direita = area_total - area_esquerda;

    if (area_esquerda == area_direita) {
        cout << 0 << endl;
    } else if (area_esquerda > area_direita) {
        cout << 1 << endl;
    } else {
        cout << 2 << endl;
    }

    return 0;
}