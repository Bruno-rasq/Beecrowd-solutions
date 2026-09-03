#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<string, string> dicionarioPoliglotaPapaiNoel;

    int tamanho_divionario;
    cin >> tamanho_divionario;
    cin.ignore(); // Ignora o '\n' após o número

    for (int i = 0; i < tamanho_divionario; i++) {
        string idioma, frase;
        getline(cin, idioma);
        getline(cin, frase);
        dicionarioPoliglotaPapaiNoel[idioma] = frase;
    }

    int numero_criancas;
    cin >> numero_criancas;
    cin.ignore(); // Ignora o '\n' após o número

    for (int i = 0; i < numero_criancas; i++) {
        string nome_crianca, idioma;
        getline(cin, nome_crianca);
        getline(cin, idioma);

        cout << nome_crianca << endl;
        cout << dicionarioPoliglotaPapaiNoel[idioma] << endl;
        cout << endl;
    }

    return 0;
}