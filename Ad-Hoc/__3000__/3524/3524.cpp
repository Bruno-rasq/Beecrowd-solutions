#include <iostream>
#include <string>
using namespace std;

/*
    Regras:

    ao pressionar o botão, o led mais a direita muda de estado
    (O on/ - off). caso ele apague então propaga a ação para o
    led imediatamente a esquerda 

    a propagação só acaba se o led a esquerda trocar seu estado
    para apagado. 

    quantos clicks são necessários para mudar a configuração de
    estados dos leds inicial para uma desejada?
*/

void propagation(string& leds, int pos){
    if(pos < 0) return;
    leds[pos] = (leds[pos] == 'O' ? '-' : 'O');
    if(leds[pos] == '-')
        propagation(leds, pos - 1);
}

int main() {

    int n;
    cin >> n;

    string leds; // config inicial
    cin >> leds;

    string targetConfig;
    cin >> targetConfig;

    int clicks = 0;

    while(leds != targetConfig){
        clicks++;
        leds[n - 1] = (leds[n - 1] == 'O' ? '-' : 'O');
        if(leds[n - 1] == '-'){
            propagation(leds, n - 2);
        }
    }

    cout << clicks << "\n";
    return 0;
}