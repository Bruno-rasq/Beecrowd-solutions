#include <iostream>
#include <vector>
#include <algorithm>
using namespace std; 

// HÁ UMA LISTA DE N INIMIGOS, CADA INIMIGO LEVA TI TEMPOS PARA SER
// DERROTADO, PORÉM TEMOS APENAS K TEMPOS DISPONÍVEIS. OS INIMIGOS
// DEVEM SER DERROTADOS EM SEQUÊNCIA. PROBLEMA É ACHAR A MAIOR SUBSEQUENCIA
// QUE SATISFAÇA A CONDIÇÃO DE K TEMPOS.

using LL = long long;
using TIMES = vector<long long>;

// IDEIA USAR UMA SLIDINW WINDOW, UM PONTEIRO PARA ESQUERDA, E UM PARA
// PARA DIREITA. ENQUANTO A SOMA DOS ELEMENTOS FOR MENOR OU IGUAL A K
// AUMENTA O PONTEIRO DA DIREITA, SE PASSAR O VALOR DE K AUMENTA O DA 
// ESQUERDA.

// RESPOSTA É A DIFERENÇA ENTRE O PONTEIRO DA ESQUERDA E DA DIREITA.

int main() {
    int N;
    LL K;
    cin >> N >> K;

    TIMES T(N, 0);
    for (size_t i = 0; i < N; i++)
        cin >> T[i];

    // SLIDING WINDOW 
    LL sum = 0;
    int left = 0;
    int ans = 0;
    
    for (int right = 0; right < N; right++) {
        sum += T[right];
        while (sum > K) {
            sum -= T[left];
            left++;
        }
        ans = max(ans, right - left + 1);
    }

    cout << ans << "\n";
    return 0;
}