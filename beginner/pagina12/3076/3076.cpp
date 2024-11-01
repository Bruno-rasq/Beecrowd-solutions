#include <iostream>

using namespace std;

int main(){
    int ano;

    while(cin >> ano){
        if(ano <= 100){
            cout << 1 << endl;
        } else {

            int seculo = ano / 100;
            if(ano % 100 != 0){
                seculo++;
            }
            cout << seculo << endl;
        }
    }

    return 0;
}