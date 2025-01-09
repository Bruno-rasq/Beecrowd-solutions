#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

bool jogadaPossivel(string& pi, string& pf){

    int deslocamentos[8][2] = {
        {2, 1}, {1, 2}, {-1, 2}, {-2, 1}, 
        {-2, -1}, {-1, -2}, {1, -2}, {2, -1}
    };
    map<char, int> colunas = {
        {'a',1}, {'b',2}, {'c',3}, {'d',4}, 
        {'e',5}, {'f',6}, {'g',7}, {'h', 8}
    };

    int coluna = colunas[pi[0]];
    int linha = stoi(pi.substr(1));

    for(const auto& pos: deslocamentos){
        int nova_coluna = coluna + pos[0];
        int nova_linha = linha + pos[1];

        if(nova_coluna == colunas[pf[0]] && nova_linha == stoi(pf.substr(1))){
            return true;
        }
    }
    return false;
}

int main() {

    string posicao_inicial, posicao_desejada;
    cin >> posicao_inicial >> posicao_desejada;

    bool response = jogadaPossivel(posicao_inicial, posicao_desejada);

    cout << (response ? "VALIDO" : "INVALIDO") << endl;

    return 0;
}