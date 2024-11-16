#include <iostream>

using namespace std;

int main(){

    int lp, ap, qnt;
    
    while(cin >> lp >> ap >> qnt){
        for(int i = 0; i < qnt; i++){
            int lpc, apc;
            cin >> lpc >> apc;

            bool condicoes = (
                lpc <= lp && apc <= ap || lpc <= ap && apc <= lp
            )

            if(condicoes){
                cout << "Sim" << endl;
            } else {
                cout << "Nao" << endl;
            }
        }
    }

    
    return 0;
}