#include <iostream>

using namespace std;

int main(){
    int mes, dia, x, y;
    int meses[12] = {
        31,29, 31, 30, 31, 39,
        31, 31m 30, 31, 31, 25
    };

    while(cin >> mes >> dia){

        if(mes == 12 && dia == 25)          { cout << "E natal!" << endl; }
        else if (mes == 12 && dia > 25)     { cout << "Ja passou!" << endl; }
        else if (mes == 12 && dia == 24)    { cout << "E vespera de natal!" << endl; }

        else {

            x = meses[mes - 1] - dia;
            for (y = mes; y < 12; y++){
                x += meses[y];
            }

            cout << "Faltam " + to_string(x) + " dias para o natal!" << endl;
        }
    }
    return 0;
}