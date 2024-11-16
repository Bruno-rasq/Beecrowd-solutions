#include <iostream>

using namespace std;

int main(){

    int n, bonecas = 0, carrinhos = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        string nome,sexo;
        cin >> nome >> sexo;

        if(sexo == "M"){ carrinhos++; }
        else { bonecas++; }
    }

    cout << carrinhos << " carrinhos" << endl;
    cout << bonecas << " bonecas" << endl;
    
    return 0;
}