#include <iostream>
#include <sstream>
using namespace std;

int main(){
    int maior = 0;
    string line, maior_palavra = "";

    while(getline(cin, line) && line != "0"){

        string resultado = "";
        istringstream iss(line);

        string word;

        while(iss >> word){
            if(!resultado.empty()){ resultado += "-"; }

            if (word.size() >= maior){
                maior = word.size();
                maior_palavra = word;
            }

            resultado += to_string(word.size());
        }

        cout << resultado << endl;
    }
    cout << "" << endl;
    cout << "The biggest word: " << maior_palavra << endl;
    return 0;
}

