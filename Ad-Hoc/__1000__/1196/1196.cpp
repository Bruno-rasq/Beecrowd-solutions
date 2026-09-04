#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

typedef vector<char> TECLAS;
typedef vector<TECLAS> TECLADO;

int main() {
    TECLADO teclado = {
        {'`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='},
        {'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'},
        {'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\''},
        {'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'}
    };

    // Criar um mapa de substituição
    unordered_map<char, char> mapeamento;
    for (const TECLAS& linha : teclado) {
        for (size_t i = 1; i < linha.size(); i++) {  
            mapeamento[linha[i]] = linha[i - 1];  // Mapeia cada tecla para a anterior
        }
    }

    string inputline;
    while (getline(cin, inputline)) {
        string output;
        for (char c : inputline) {
            if (c == ' ') {  
                output += ' ';  // Mantém espaços
            } else if (mapeamento.find(c) != mapeamento.end()) {  
                output += mapeamento[c];  // Substitui pela tecla anterior
            } else {  
                output += c;  // Mantém caracteres não mapeados
            }
        }
        cout << output << endl;
    }

    return 0;
}