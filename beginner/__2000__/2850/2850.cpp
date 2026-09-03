#include <iostream>
using namespace std;

int main(){
    string input;

    while(getline(cin, input)){
        if(input == "esquerda"){ cout << "ingles" << endl; }
        if(input == "direita"){ cout << "frances" << endl; }
        if(input == "nenhuma"){ cout << "portugues" << endl; }
        if(input == "as duas"){ cout << "caiu" << endl; }
    }
    return 0;
}