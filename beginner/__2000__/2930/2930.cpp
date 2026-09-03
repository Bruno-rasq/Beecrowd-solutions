#include <iostream>
using namespace std;

int main(){

    int entrega, prazo;
    cin >> entrega >> prazo;

    if (prazo - entraga >= 1){

        cout << "Muito bem!, Apresenta antes do Natal!" << endl;
    }

    else if (prazo - entraga < 0){

        cout << "Eu te odeio professora!" << endl;
    }

    else if (prazo - entraga < 3){

        cout << "Parece o trabalho do meu filho!" << endl;
        prazo += 2;
        if (prazo <= 24){

            cout << "TCC Apresentado!" << endl;
        }
        else{

            cout << "Fail! Entao eh nataaaaal!" << endl;
        }
    }
    return 0;

}