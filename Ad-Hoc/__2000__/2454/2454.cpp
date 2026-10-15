#include <iostream>
using namespace std;

// Há duas comportas P e R, se P for 0 resposta C, senão deve
// verificar a comporta R, se for 0 resposta B senao A.
int main() {
    int P, R;
    cin >> P >> R;
    if (P == 0)
        cout << "C\n";
    else
        cout << (R == 0 ? "B" : "A") << "\n";
    return 0;
}