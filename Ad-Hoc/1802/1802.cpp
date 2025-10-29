#include <iostream>
#include <vector>
#include <algorithm> // para sort
using namespace std;

int main() {
    vector<vector<int>> livros(5);
    for (int i = 0; i < 5; i++) {
        int n;
        cin >> n;
        livros[i].resize(n);
        for (int j = 0; j < n; j++) cin >> livros[i][j];
    }

    int K;
    cin >> K;

    vector<int> combinacoes;

    // Geração de todas as combinações (produto cartesiano)
    for (int a : livros[0]) {
        for (int b : livros[1]) {
            for (int c : livros[2]) {
                for (int d : livros[3]) {
                    for (int e : livros[4]) {
                        combinacoes.push_back(a + b + c + d + e);
                    }
                }
            }
        }
    }

    // Ordena em ordem decrescente
    sort(combinacoes.begin(), combinacoes.end(), greater<int>());

    // Soma dos K primeiros valores
    long long soma = 0;
    for (int i = 0; i < K && i < (int)combinacoes.size(); i++) {
        soma += combinacoes[i];
    }

    cout << soma << endl;

    return 0;
}