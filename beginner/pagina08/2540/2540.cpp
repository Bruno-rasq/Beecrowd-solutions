#include <iostream>

using namespace std;

int main() {

    int jogadores;

    while(cin >> jogadores){

        int voto, votosImpeachment = 0;
        double doisTercos = jogadores * (2.0 / 3.0);

        for(int i = 0; i < jogadores; i++){
            cin >> voto;
            if (voto == 1)
                votosImpeachment++;
        }

        cout << (votosImpeachment >= doisTercos ? "impeachment" : "acusacao arquivada") << endl;
    }
    return 0;
}