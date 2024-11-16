#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Spell {
    string nome;
    int dano;
    vector<int> nivel;
}

Spell spells[] = {
    {"fire",  200,  {20, 30, 50}},
    {"earth", 400,  {25, 55, 70}},
    {"water", 300,  {10, 25, 40}},
    {"air",   100,  {18, 38, 60}}
};

int main(){
    int t;
    cin >> t;

    for(int i = 0; i < t; i++){
        int w, h, x0, y0;
        cin >> w >> h >> x0 >> y0;

        string magia;
        int nivel, cx, cy;
        cin >> magia >> nivel >> cx >> cy;

        Spell spell = {"", 0, {}};
        for(const auto& s: spells){
            if(s.nome == magia){
                spell = s;
                break;
            }
        }

        int dano = spell.dano;
        int raio = spell.nivel[nivel - 1];

        int esquerda = x0, direita = x0 + w, baixo = y0, cima = y0 + h;

        int ponto_mais_proximo_x = max(esquerda, min(cx, direita));
        int ponto_mais_proximo_y = max(baixo, min(cy, cima));

        double distancia = 
        (ponto_mais_proximo_x - cx) * (ponto_mais_proximo_x - cx) +
        (ponto_mais_proximo_y - cy) * (ponto_mais_proximo_y - cy);

        if(distancia <= raio){
            cout << dano << endl;
        } else {
            cout << 0 << endl;
        }
    }

    return 0;
}