#include <iostream>
using namespace std;

int main() {
    int L, C, X, Y;
    cin >> L >> C >> X >> Y;

    int index = X * C + Y;

    if (index % 2 == 0)
        cout << "Direita\n";
    else
        cout << "Esquerda\n";

    return 0;
}