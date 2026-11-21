#include <iostream>
#include <cmath>
using namespace std;

/*
    Há um robo em um grid infinito, esse robo tem coordenada XY
    e deseja ir para uma coordenada específica com no máximo K passos.

    programa pede para calcular se é possível ou não executar tal
    tarefa.
*/

int main() {

    int x1, y1, x2, y2, k;
    cin >> x1 >> y1 >> x2 >> y2 >> k;

    // distancia de Manhattan
    int D = abs(x2 - x1) + abs(y2 - y1);

    cout << (D <= k ? "SIM" : "NAO") << "\n";

    return 0;
}