#include <iostream>
#include <iomanip>
#define NOVO_VOLUME(vcurr, vvar)(max(0, min(100, vcurr + vvar)))
using namespace std;

int main(){

    int vol_atual, trocas, alt;
    cin >> vol_atual >> trocas;

    for(int i = 0; i < trocas; i++){
        cin >> alt;
        int novo_volume = NOVO_VOLUME(vol_atual, alt);
        vol_atual = novo_volume;
    }

    cout << vol_atual << endl;

    return 0;
}