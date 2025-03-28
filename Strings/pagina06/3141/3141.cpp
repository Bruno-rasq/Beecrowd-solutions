#include <iostream>

using namespace std;

int main(){

    string nome, data1, data2;
    int dia_atual, mes_atual, ano_atual;
    int dia_nasci, mes_nasci, ano_nasci;

    getline(cin, nome);
    scanf("%d/%d/%d", &dia_atual, &mes_atual, &ano_atual);
    scanf("%d/%d/%d", &dia_nasci, &mes_nasci, &ano_nasci);

    
    if(dia_nasci == dia_atual && mes_nasci == mes_atual){
        cout << "Feliz aniversario!" << endl;
    }

    int idade = ano_atual - ano_nasci;
    if(mes_atual < mes_nasci || (mes_atual == mes_nasci &&  dia_atual < dia_nasci)){
        idade -= 1;
    }

    cout << "Voce tem " + to_string(idade) + " anos " + nome + "." << endl;

    return 0;
}