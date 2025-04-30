#include <iostream>
#include <string>
using namespace std;

void wordplay(const string& palavra, int caso) {
    string menor = palavra;
    string maior = palavra;
    string dupla = palavra + palavra;

    for (int j = 1; j < palavra.size(); j++) {
        string rotacionada = dupla.substr(j, palavra.size());
        if (rotacionada < menor) menor = rotacionada;
        if (rotacionada > maior) maior = rotacionada;
    }

    cout << "Caso " << caso << ": " << menor << " " << maior << endl;
}

int main() {
    string palavra;
    int i = 1;
    while (cin >> palavra && palavra != "*") {
        wordplay(palavra, i);
        i++;
    }
    return 0;
}
