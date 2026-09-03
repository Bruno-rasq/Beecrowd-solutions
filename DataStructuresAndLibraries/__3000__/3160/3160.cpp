#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string lista_atual, nova_lista, amigo_indicado;

    getline(cin, lista_atual);
    getline(cin, nova_lista);
    getline(cin, amigo_indicado);

    size_t pos = lista_atual.find(amigo_indicado);
    
    if (pos != string::npos && amigo_indicado != "nao") {
        // Inserindo a nova lista ANTES do amigo indicado
        if (pos > 0 && lista_atual[pos - 1] != ' ') {
            lista_atual.insert(pos, " " + nova_lista);
        } else {
            lista_atual.insert(pos, nova_lista + " ");
        }
    } else {
        // Inserindo a nova lista no final sem espaços extras
        if (!lista_atual.empty()) {
            lista_atual += " " + nova_lista;
        } else {
            lista_atual = nova_lista;
        }
    }

    cout << lista_atual << endl;

    return 0;
}