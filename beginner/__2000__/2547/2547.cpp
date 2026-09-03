#include <iostream>

using namespace std;

int main() {

    int participantes, altura_minima, altura_maxima, altura;

    while (cin >> participantes >> altura_minima >> altura_maxima){


        int total_participantes_habeis = 0;
        for(int i = 0; i < participantes; i++){
            cin >> altura;

            if(altura >= altura_minima && altura <= altura_maxima){
                total_participantes_habeis++;
            }

        }
        
        cout << total_participantes_habeis << endl;
    }
}