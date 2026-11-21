#include <iostream>
using namespace std;

int main() {

    int itens;
    cin >> itens;

    int arco = 0;
    int escudo = 0;
    int espada = 0;
    int pocao = 0;

    for(size_t i = 0; i < itens; i++){
        string item;
        cin >> item;

        if(item == "arco") arco++;
        if(item == "escudo") escudo++;
        if(item == "espada") espada++;
        if(item == "pocao") pocao++;
    }

    cout << "arco " << arco << "\n";
    cout << "escudo " << escudo << "\n";
    cout << "espada " << espada << "\n";
    cout << "pocao " << pocao << "\n";

    return 0;
}