#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<string> split(const string& str) {
    stringstream ss(str);
    string palavra;
    vector<string> palavras;
    while (ss >> palavra) {
        palavras.push_back(palavra);
    }
    return palavras;
}

string corrigir_palavra(const string& palavra) {
    if (palavra.length() == 10 && palavra.substr(1, 8) == "oulupukk") {
        return "Joulupukki";
    } else if (palavra.length() == 11 && palavra.substr(1, 8) == "oulupukk" && palavra.back() == '.') {
        return "Joulupukki.";
    }
    return palavra;
}

int main() {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);

        vector<string> mensagem = split(line);
        vector<string> corrigida;

        for (const auto& palavra : mensagem) {
            corrigida.push_back(corrigir_palavra(palavra));
        }

        // Imprime a mensagem corrigida unindo as palavras com espaço
        for (size_t j = 0; j < corrigida.size(); j++) {
            cout << corrigida[j];
            if (j < corrigida.size() - 1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}
