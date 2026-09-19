#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

// CADA UM DOS N SOLDADOS COMEÇAM COM 0 PONTOS, HAVERÁ M CONSULTAS
// UMA CONSULTA POSSUE UM VALOR LEFT, RIGHT. TODOS OS SOLDADOS ENTRE
// L E R RECEBEM MAIS 1 PONTO 

// NO FINAL VAI TER X PONTOS (MAXIMO) E Y SOLDADOS COM ESSA QUANTIDADE
// DE PONTOS. O PROGRAMA PEDE O VALOR DE X E Y E QUAIS SÃO OS Y SOLDADOS.

int main(){
    int n, q;
    cin >> n >> q;

    vector<int> diff(n + 1, 0);

    for(int i = 0; i < q; i++){
        int left, right;
        cin >> left >> right;

        diff[left - 1]++;
        diff[right]--;
    }

    int max_score = 0;
    int score = 0;

    vector<int> scores(n);

    for(int i = 0; i < n; i++){
        score += diff[i];
        scores[i] = score;

        if(score > max_score)
            max_score = score;
    }

    stringstream buffer;
    int count = 0;

    for(int i = 0; i < n; i++){
        if(scores[i] == max_score){
            buffer << i + 1 << "\n";
            count++;
        }
    }

    cout << max_score << " " << count << "\n";
    cout << buffer.str();

    return 0;
}