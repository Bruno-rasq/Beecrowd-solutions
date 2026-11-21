#include <iostream>
using namespace std;

int main() {
    int password;
    while(cin >> password){
        if(password == 2002){
            cout << "Acesso Permitido\n";
            break;
        }
        else
            cout << "Senha Invalida\n";
    }
    return 0;
}