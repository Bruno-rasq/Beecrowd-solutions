#include <iostream>
#include <algorithm> // Para usar std::max

using namespace std;

bool isTriangle(int a, int b, int c) {
    return (a + b) > c && (b + c) > a && (a + c) > b;
}

bool isTriangleRetan(int a, int b, int c) {
    int maior = max({a, b, c});
    int menor1, menor2;

    if (maior == a) {
        menor1 = b;
        menor2 = c;
    } else if (maior == b) {
        menor1 = a;
        menor2 = c;
    } else {
        menor1 = a;
        menor2 = b;
    }

    return (menor1 * menor1) + (menor2 * menor2) == (maior * maior);
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    if (!isTriangle(a, b, c)) {
        cout << "Invalido" << endl;
    } else {
        if (a == b && b == c) {
            cout << "Valido-Equilatero" << endl;
        } else if (a != b && b != c && a != c) {
            cout << "Valido-Escaleno" << endl;
        } else {
            cout << "Valido-Isoceles" << endl;
        }

        cout << (isTriangleRetan(a, b, c) ? "Retangulo: S" : "Retangulo: N") << endl;
    }

    return 0;
}