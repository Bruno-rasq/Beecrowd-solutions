#include <iostream>
using namespace std;

string toBinarioString(int n){
    if(n == 0) return "0";
    string bin = "";
    while(n > 0){
        bin = (n % 2 == 0 ? "0" : "1") + bin;
        n /= 2;
    }
    return bin;
}

int main(){

    int mnv = 0;
    for(int i = 0; i < 4; i++){
        int soma = 0;
        for(int j = 0; j < 7; j++){
            int aux;
            cin >> aux;
            soma += aux;
        }
        if(soma > mnv) mnv = soma;
    }

    cout << to_string(mnv) + " = " + toBinarioString(mnv) << endl;
    return 0;
}