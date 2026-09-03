#include <iostream>

using namespace std;

int main(){

    int h1, m1, h2, m2;
    cin >> h1 >> m1 >> h2 >> m2;

    int hr, min;

    if(h2 < h1 || (h2 == h1 && m2 < m1)){
        h2 += 24;
    }

    if(m2 < m1){
        m2 += 60;
        h2 -= 1;
    }

    hr = h2 - h1;
    min = m2 - m1;

    if(hr == 0 && min == 0){
        hr = 24;
        min = 0;
    }

    cout << "O JOGO DUROU "  << hr << " HORA(S) E " << min << " MINUTO(S)\n";

    return 0;
}