#include <iostream>
#include <vector>

using namespace std;

void criarCrianca(string nome, vector<string>& list){
    list.push_back(nome);
    list.push_back(nome);
}

int main() {

    int n, index = 0;
    cin >> n;

    vector<string> criancas;

    criancas.push_back("joao");
    criancas.push_back("joao");

    for(int i = 0; i < n - 1; i++){
        criarCrianca("crianca" + to_string(i + 2), criancas);
    }

    while(criancas.size() > 1){
        index = (index + 28) % criancas.size();
        criancas.erase(criancas.begin() + index);
    }

    if(criancas[0] == "joao")
        cout << "vai ganhar" << endl;
    else
        cout << "nao vai ganhar" << endl;

    return 0;
}