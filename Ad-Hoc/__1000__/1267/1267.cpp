#include <iostream>
#include <vector>

using namespace std;

int main(){
    int num_ex_alunos, num_eventos;
    cin  >> num_ex_alunos >> num_eventos;

    if(num_ex_alunos == 0 && num_eventos == 0) break;

    vector<int> contagem_participacoes;
    for(int i = 0; i < num_ex_alunos; i++)
        contagem_participacoes.push_back(0);

    for(int i = 0; i < num_eventos; i++){
        vector<int> participacoes;
        for(int j = 0; j < num_ex_alunos; j++){
            int participacao;
            cin >> participacao;
            participacoes.push_back(participacao);
        }
        for(int j = 0; j < participacoes.size(); j++){
            contagem_participacoes[j] += participacoes[j];
        }
    }

    // ...continuar print("yes" if num_eventos in contagem_participacoes else "no")
}
