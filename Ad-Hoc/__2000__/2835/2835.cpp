#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// OBJETIVO: LEVAR TODAS AS CAIXAS DO PRIMEIRO ANDAR PARA O SEGUNDO
// USANDO O ELEVADOR DE POLIA (DESCONSIDERANDO A FISICA) A ÚNICA CONDIÇÃO
// PARA UMA CAIXA DE PESO N SUBIR É QUE A DIFERENÇA ENTRE AS CABINES P E Q
// SEJA <= 8.

// QUANDO A TROCA ACONTECE O QUE TA EMBAIXO VAI PARA CIMA E O QUE ESTÁ
// EM CIMA VAI PARA BAIXO, SE UMA CAIXA TIVER PESO <= 8 ELA PODE SUBIR
// SOZINHA.

const int CONDITION = 8;

// SE A DIFERENÇA ENTRE DUAS CAIXAS CONSECUTIVAS FOR MAIOR QUE 8,
// NÃO É POSSÍVEL LEVAR TODAS AS CAIXAS PARA O SEGUNDO ANDAR.
//
// AS CAIXAS SÃO ORDENADAS PARA QUE POSSAMOS VERIFICAR A DIFERENÇA
// ENTRE CADA CAIXA E A ANTERIOR, COMEÇANDO PELO PESO 0 DA CABINE VAZIA.

int main() {

    int n;
    cin >> n;

    vector<int> boxes(n);
    for (int i = 0; i < n; i++) {
        cin >> boxes[i];
    }

    // ORDENA AS CAIXAS EM ORDEM CRESCENTE
    sort(boxes.begin(), boxes.end());

    // O PONTO DE PARTIDA É UMA CABINE VAZIA
    int current_weight = 0;

    for (int box_weight : boxes) {

        // SE A DIFERENÇA ENTRE A CAIXA ATUAL E A ANTERIOR
        // FOR MAIOR QUE 8, NÃO É POSSÍVEL CONTINUAR
        if (box_weight - current_weight > CONDITION) {
            cout << "N\n";
            return 0;
        }

        current_weight = box_weight;
    }

    cout << "S\n";
    return 0;
}