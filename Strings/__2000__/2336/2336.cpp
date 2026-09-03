//dado um valor N de base ABC devo converter para base 10
//para isso é necessário pegar o indice de cada caracter na tabela
//ASCII - 65, isso porque A em ASCII é 65 mas na base ABC é 0.

//tendo os valores da de cada caracter deve então converte para base 10
//resultado = (resultado * 26 + valor) % (10^9 + 7)

#include <iostream>
using namespace std;

int main() {
    string abc;
    const int MOD = 1000000007;

    while (cin >> abc) {
        int resultado = 0;
        for (const char& chr : abc) {
            int codigo = chr - 'A';
            resultado = (1LL * resultado * 26 + codigo) % MOD;
        }

        cout << resultado << endl;
    }

    return 0;
}
