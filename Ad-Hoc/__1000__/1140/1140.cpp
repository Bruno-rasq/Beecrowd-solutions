#include <iostream>
#include <vector>
#include <cctype>
#include <sstream>
using namespace std;

bool isTautogram(vector<string>& palavras) {
    vector<char> primeirosChar;
    for (const string& palavra : palavras) {
        primeirosChar.push_back(tolower(palavra[0]));  // Corrigido aqui
    }
    
    char charInicial = primeirosChar[0];  // Deve ser char, não string
    for (const char& c : primeirosChar) {
        if (c != charInicial) return false;
    }
        
    return true;
}

int main() {
    string line;
    while (getline(cin, line)) {  // getline para ler a linha inteira
        if (line == "*") break;
        
        stringstream ss(line);
        vector<string> palavras;
        string palavra;
        while (ss >> palavra) {
            palavras.push_back(palavra);
        }
        
        bool response = isTautogram(palavras);
        cout << (response ? "Y" : "N") << endl;
    }
    return 0;
}