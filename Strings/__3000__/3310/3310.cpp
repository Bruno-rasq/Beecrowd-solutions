#include <iostream>
#include <vector>
#include <algorithm> // min, max, swap

using namespace std;

using relief = vector<int>;

int simular(relief chao, relief teto) {
    int n = chao.size();
    int trocas = 0;
    int nivel_atual = chao[0];

    for (int i = 1; i < n; i++) {
        int proximo = chao[i];

        if (proximo == 0 || proximo > nivel_atual) {
            swap(chao, teto);         // troca os vetores
            nivel_atual = chao[i - 1]; // pega o nível anterior após a troca
            trocas++;
        } else {
            nivel_atual = proximo;
        }
    }

    return trocas;
}

int main() {
    int N;
    while (cin >> N) {
        relief teto(N), chao(N);

        for (int i = 0; i < N; i++) cin >> teto[i];
        for (int i = 0; i < N; i++) cin >> chao[i];

        // tenta começar no chão e no teto
        int resultado_chao = simular(chao, teto);
        int resultado_teto = simular(teto, chao);

        int menor = min(resultado_chao, resultado_teto) + 1;
        int maior = max(resultado_chao, resultado_teto) - 1;

        cout << min(menor, maior) << "\n";
    }
    return 0;
}