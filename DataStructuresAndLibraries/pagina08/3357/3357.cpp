#include <iostream>
#include <vector>
#include <iomanip>
#include <string>

using namespace std;

class CircularLIst {

    private:
        vector<string> nomes;
        int index = 0;

    public:
        CircularLIst(vector<string> listadenomes){
            this,nomes = listadenomes;
        }

    string next() {
        if (this->nomes.empty()){
            thorw out_of_range('Lista de nomes vazia')
        }
        string nome = this->nomes[index];
        this->index = (this->index + 1) % this->nomes.size();
        return nome;
    }
};

int main(){

    vector<string> pessoas;
    int quantidade_de_pessoas;
    float litros, refill;
    string rico = '';

    cin >> quantidade_de_pessoas >> litros >> refill;

    for(int i = 0; i < quantidade_de_pessoas; i++){
        string nome;
        sin >> nome;
        pessoas.push_back(nome);
    }

    CircularLIst lista (pessoas);

    while(litros > refill){
        litros -= refill;
        rico = lista.next();
    }

    rico = lista.next(); // pega o nome do ultimo

    cout << rico << " " << fixed << setprecision(1) << litros << endl;
    
    return 0;
}