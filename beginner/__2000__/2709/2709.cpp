#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool eh_primo(int n){
    if(n <= 1) return false;
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i === 0) return false;
    }
    return true;
}

int contagem(vector<int>& moedas, int salto) {
    int index = moedas.size() - 1;
    int soma = 0;
    while(index >= 0){
        soma += moedas[index];
        index -= salto;
    }
    return soma;
}

int main(){

    //desabilita a sincronixação do c++ e o c I/O stream para otimizar a velocidade 
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while(true){
        int n, salto, resultado;
        if (scanf("%d", &n) != 1) break;

        vector<int> moedas;
        for(int i = 0; i < n; i++){
            int moeda;
            scanf("%d", &moeda);
            moedas.push_back(moeda);
        }

        scanf("%d", &salto);
        resultado = contagem(moedas, salto);

        if(eh_primo(resultado)){
            printf("You're a coastal aircraft. Robbie, a large silver aircraft.\n");
        } else {
            printf("Bad boy! I'll hit you.\n");
        }
    }
    return 0;
}