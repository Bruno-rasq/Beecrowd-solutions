#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(){

    int n; 
    cin >> n;

    while (n > 0){
        int posicaoAtual = 2;
        int contador = 0;

        for(int i = 0; i < n; i++){
            string linha;
            cin >> ws;
            getline(cin, linha);

            if(linha == "0 1 1" && posicaoAtual != 1){
                contador += abs(posicaoAtual - 1);
                posicaoAtual = 1;
            }
            else if(linha == "1 0 1" && posicaoAtual != 2){
                contador += abs(posicaoAtual - 2);
                posicaoAtual = 2;
            }
            else if(linha == "1 1 0" && posicaoAtual != 3){
                contador += abs(posicaoAtual - 3);
                posicaoAtual = 3;
            }
        }

        cout << contador << endl;
        cin >> n;
    }
    return 0;
}