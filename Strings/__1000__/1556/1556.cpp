#include <iostream>
#include <set>
#include <sstream>
using namespace std;

/*
    OBJETIVO, ESCREVER TODAS AS COMBINAÇÕES (PERMUTAÇÕES) DE UMA
    STRING INPUT EM ORDEM ALFABÉTICA E SEQUÊNCIAL REMOVENDO ALGUMAS
    LETRAS POR VEZ.

    A ESTRUTURA SET ARMAZENA AS COMBINAÇÕES ÚNICAS GERADAS EM ORDEM
    LEXICOGRÁFICA, O QUE AUXILIA NA ORDENAÇÃO.
*/

void register_Combination(set<string>& comb, string word){

    comb.insert(word);

    for(size_t idx = 0; idx < word.size(); idx++){
        string curr_comb = word.substr(0, idx) + word.substr(idx + 1);

        if(comb.find(curr_comb) == comb.end() && !curr_comb.empty()){
            register_Combination(comb, curr_comb);
        }
    }
}

int main() {

    string input;
    stringstream output;

    while(cin >> input){

        set<string> combinations;
        register_Combination(combinations, input);

        for(const auto& comb : combinations)
            output << comb << "\n";

        output << "\n";
    }

    cout << output.str();

    return 0;
}
