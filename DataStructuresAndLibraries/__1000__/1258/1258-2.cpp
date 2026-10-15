#include <iostream>
#include <sstream>
#include <unordered_map>
#include <map>
using namespace std;

/*
    ORGANIZAR PEDIDOS DE CAMISETAS POR COR, TAMANHO E NOME DO PEDINTE.
    
    COR: BRANCAS PRIMEIRO E DEPOIS VERMELHAS.
    TAMANHO: P, M ,G
    NOME: ORDEM ALFABÉTICA LEXICOGRAFICA.
*/

#define LIST map<string, int>
#define SET unordered_map<string, LIST>
#define GROUP unordered_map<string, SET>

void LOG(const GROUP& data, const string& color, const string& s){
    stringstream buffer;

    for(const auto& [name, quantity] : data.at(color).at(s))
        for(int i = 0; i < quantity; i++)
            buffer << color << " " << s << " " << name << "\n";

    cout << buffer.str();
}


int main() {

    bool first_test_case = true;
    int n;

    while((cin >> n) && (n != 0)){

        GROUP data = {
            {"branco", {{"P", {}}, {"M", {}}, {"G", {}}}},
            {"vermelho", {{"P", {}}, {"M", {}}, {"G", {}}}}
        };

        cin.ignore();

        for(size_t i = 0; i < n; i++){
            string name, color, shirt_size;

            getline(cin, name);
            cin >> color >> shirt_size;
            cin.ignore();

            data[color][shirt_size][name]++;
        }

        if(!first_test_case)
            cout << "\n";

        first_test_case = false;
        LOG(data, "branco", "P");
        LOG(data, "branco", "M");
        LOG(data, "branco", "G");
        LOG(data, "vermelho", "P");
        LOG(data, "vermelho", "M");
        LOG(data, "vermelho", "G");
    }

    return 0;
}