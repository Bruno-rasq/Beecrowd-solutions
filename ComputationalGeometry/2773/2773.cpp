#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// CALCULA A MENOR DISTÂNCIA ENTRE CASA E ESCOLA,
// CONTORNANDO O TERRENO POR CIMA OU POR BAIXO.
double distance(
    int xi, int yi,
    int xf, int yf,
    int x1, int y1,
    int xr, int yr
) {
    // CAMINHO PASSANDO PELA BORDA INFERIOR.
    double bottom =
        hypot(x1 - xi, y1 - yi) +
        (xr - x1) +
        hypot(xf - xr, yf - y1);

    // CAMINHO PASSANDO PELA BORDA SUPERIOR.
    double top =
        hypot(x1 - xi, yr - yi) +
        (xr - x1) +
        hypot(xf - xr, yf - yr);

    return min(bottom, top);
}

int main() {

    int xi, yi, xf, yf, velocity;
    while (cin >> xi >> yi >> xf >> yf >> velocity) {

        int x1, y1, xr, yr;
        cin >> x1 >> y1 >> xr >> yr;

        double dist = distance(
            xi, yi,
            xf, yf,
            x1, y1,
            xr, yr
        );

        double time = dist / velocity;
        cout << fixed << setprecision(1) << time << '\n';
    }
    return 0;
}