#include <iostream>
#include <string>
using namespace std;

int main(){

    string becteria_dna, code_genetico;

    while(getline(cin, becteria_dna) and getline(cin, code_genetico)){

        if(becteria_dna.find(code_genetico) != string::npos){
            cout << "Resistente\n";
        } else {
            cout << "Nao resistente\n";
        }
    }

    return 0;
}