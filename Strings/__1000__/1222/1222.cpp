#include <iostream>
#include <vector>

using namespace std;

int main(){

    int total_palavras, max_linha, max_char;

    while (cin >> total_palavras >> max_linha >> max_char){

        vector<string> conto;
        for(int i = 0; i < total_palavras; i++){
            string palavra;
            cin >> palavra;
            conto.push_back(palavra);
        }
        int qnt_paginas = 0, ind = 0;

        while (ind < conto.size()) {
            int linhas = 0;
            while (linhas < max_linha && ind < conto.size()) {
                int linha_len = 0;
                while (ind < conto.size()) {
                    string palavra = conto[ind];
                    if (linha_len == 0) {
                        if (palavra.size() <= max_char) {
                            linha_len = palavra.size();
                            ind++;
                        } else {
                            break;
                        }
                    } else if (linha_len + 1 + palavra.size() <= max_char) {
                        linha_len += 1 + palavra.size();
                        ind++;
                    } else {
                        break;
                    }
                }
                linhas++;
            }
            qnt_paginas++;
        }

        cout << qnt_paginas << endl;
    }

    return 0;
}