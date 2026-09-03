#include <iostream>
#include <sstream>
#include <algorithm> // para transform()
using namespace std;

int main() {
    string line;
    while(getline(cin, line)) {
        stringstream ss(line);
        string palavra;

        string cobol = "cobol";
        bool valido = true;

        int ind = 0;
        while(getline(ss, palavra, '-')) {
            // Transforma a palavra em minúscula
            transform(palavra.begin(), palavra.end(), palavra.begin(), ::tolower);

            char letra = cobol[ind];
            if (palavra.front() != letra && palavra.back() != letra) {
                valido = false;
                break;
            }
            ind++;
        }

        cout << (valido ? "GRACE HOPPER" : "BUG") << endl;
    }

    return 0;
}
