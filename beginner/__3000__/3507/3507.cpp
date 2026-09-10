#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long number_animais, number_legs; 
    cin >> number_animais >> number_legs;

    // TOTAL DE ANIMAIS = NUMERO DE GANSOS + NUMERO DE TIGRES
    // NUMERO DE TIGRES = TOTAL DE ANIMAIS - NUMERO DE GANSOS

    // LEGS = (2 * GANSOS) + (4 * TIGRES)
    // LEGS = (2 * GANSOS) + (4 * (N_ANIMAIS - GANSOS))
    // LEGS = 2*GANSOS + 4*N_ANIMAIS - 4*GANSOS
    // LEGS - 4*N_ANIMAIS = 2*GANSOS - 4*GANSOS
    // LEGS - 4*N_ANIMAIS = -2*GANSOS
    // GANSOS = (LEGS - (4 * N_ANIMAIS)) / -2

    long long G = abs(number_legs - (4 * number_animais)) / 2;
    long long T = number_animais - G;

    cout << T << "\n" << G << "\n";

    return 0;
}