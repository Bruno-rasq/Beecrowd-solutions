#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int n;
    cin >> n;

    int total = 0;
    int coelhos = 0;
    int sapos = 0;
    int ratos = 0;

    for(size_t i = 0; i < n; i++){

        int qnt;
        char type;
        cin >> qnt >> type;

        switch (type) {
            case 'C': { coelhos += qnt; break; }
            case 'R': { ratos += qnt; break; }
            case 'S': { sapos += qnt; break; }
            default: { break; }
        }

        total += qnt;
    }

    float pc = (coelhos * 100.0) / total;
    float pr = (ratos * 100.0) / total;
    float ps = (sapos * 100.0) / total;

    cout << "Total: " << total << " cobaias\n";
    cout << "Total de coelhos: " << coelhos << "\n";
    cout << "Total de ratos: " << ratos << "\n";
    cout << "Total de sapos: " << sapos << "\n";
    cout << "Percentual de coelhos: " << fixed << setprecision(2) << pc << " %\n";
    cout << "Percentual de ratos: " << fixed << setprecision(2) << pr << " %\n";
    cout << "Percentual de sapos: " << fixed << setprecision(2) << ps << " %\n";

    return 0;
}