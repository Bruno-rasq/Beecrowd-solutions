#include <iostream>
using namespace std;

const int PI = 3;

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    // x = hipotenusa
    // y e z = catetos
    if ((y*y) + (z*z) != (x*x)) cout << "Nao eh retangulo!\n";
    else {
        double raio = z / 2.0;
        double area_triangulo = (y * z) / 2;
        double area_semicirculo = (PI * (raio * raio)) / 2;
        double area_total = area_triangulo + area_semicirculo;

        cout << "AREA = " << (int)area_total << "\n";
    }
}