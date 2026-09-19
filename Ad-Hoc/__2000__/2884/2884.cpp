#include <iostream>
#include <vector>
using namespace std;

// HÁ N INTERRUPTORES PARA M LAMPADAS, CADA INTERRUPTOR MUDA O ESTADO
// DE UM CONJUNTO DE LÂMPADAS. A IDEIA É SAIR DE UM ESTADO ATUAL PARA
// UM ESTADO ONDE TODAS AS LÂMPADAS FORAM DESLIGADAS.

// NO PROBLEMA VAI SER TENTADO DESLIGAR OS INTERRUPTORES NA SEQUÊNCIA 
// 1, 2, 3.. N, 1, 2, 3..N. SE NÃO FOR POSSÍVEL APAGAR TODAS RETORNA -1
// SE NÃO RETORNA A QUANTIDADE MÍNIMA DE AÇÕES.

// LIGA: MUDA O ESTADO DO BIT(LÂMPADA) DE 0(APAGADO) PARA 1(LIGADO).
// Dividimos a lâmpada por 32 para saber qual inteiro no vetor ela pertence.
void ON(vector<int>& state, int lamp) { 
    state[lamp / 32] |= (1 << (lamp % 32)); 
}

// APLICA A MASCARA REFERENTE AO INTERRUPTOR ACIONADO.
void APPLYMASK(vector<int>& state, const vector<int>& mask) { 
    for(size_t i = 0; i < state.size(); i++) {
        state[i] ^= mask[i];
    }
}

// FUNÇÃO AUXILIAR: Verifica se todas as lâmpadas foram apagadas (tudo zero).
bool IS_TARGET_STATE(const vector<int>& state) {
    for(int val : state) {
        if(val != 0) return false;
    }
    return true;
}

int main() {
    // Otimização de entrada/saída (importante para o Beecrowd)
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // Como M vai até 1000, precisamos de (1000 / 32) + 1 inteiros para cobrir todas as lâmpadas.
    int tamanho_vetor = (M / 32) + 1;

    // SETTA O ESTADO INICIAL DAS LAMPADAS.
    vector<int> state(tamanho_vetor, 0);
    int on, lamp;
    cin >> on;
    while(on--){
        cin >> lamp;
        ON(state, lamp);
    }
    const vector<int> initial_state = state;

    // CRIANDO UMA MASCARA DE BITS PARA CADA INTERRUPTOR, QUANDO UM
    // INTERRUPTOR FOR CLICADO DEVE MUDAR O ESTADO ATUAL DE CADA LAMPADA
    // ASSOCIADA AQUELE INTERRUPTOR.
    vector<vector<int>> maskbits;
    for(int i = 0; i < N; i++){
        int lamps, l;
        vector<int> mask(tamanho_vetor, 0);
        cin >> lamps;
        while(lamps--){
            cin >> l;
            ON(mask, l);
        }
        maskbits.push_back(mask);
    }

    // TENTA ACIONAR CADA UM DOS INTERRUPTORES NA SEQUÊNCIA 1, 2, 3.. N
    // EM LOOP. Se passar de 2 * N ações sem sucesso, caímos em ciclo infinito.
    int actions = 0;
    int interuptor = 0;
    int limite_maximo = 2 * N;

    while(true){
        // Verifica se todas as lâmpadas foram apagadas antes de aplicar o próximo passo
        if (IS_TARGET_STATE(state))
            break;

        if (actions >= limite_maximo) {
            actions = -1;
            break;
        }

        APPLYMASK(state, maskbits[interuptor]);
        actions++;
        
        interuptor = (interuptor + 1) % N;
    }

    cout << actions << "\n";

    return 0;
}
