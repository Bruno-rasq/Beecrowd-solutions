
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

vector<string> split(const string& frase){
    vector<string> palavras;
    istringstream iss(frase);
    string palavra;
    while(iss >> palavra){
        palavras.push_back(palavra);
    }
    return palavras;
}

int media_frase(const vector<string>& frase) {
    int total_palavras = 0;
    int somatoria_palavras = 0;

    for (string palavra : frase) {
        if (!palavra.empty() && palavra.back() == '.') {
            palavra.pop_back();
        }

        // Verifica se a palavra contém apenas letras do alfabeto
        bool is_alpha = true;
        for (char c : palavra) {
            if (!isalpha(static_cast<unsigned char>(c))) {
                is_alpha = false;
                break;
            }
        }

        if (is_alpha) {
            somatoria_palavras += palavra.length();
            total_palavras++;
        }
    }

    if (total_palavras == 0) return 0;
    return somatoria_palavras / total_palavras;
}

int main () {
    
    string frase;
    while(getline(cin, frase)){
        vector<string> palavras = split(frase);
        int media = media_frase(palavras);
        
        cout << (media <= 3 ? 250 : (media > 3 && media <= 5 ? 500 : 1000)) << endl;
    }
    return 0;
} 