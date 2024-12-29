#include <iostream>
#include <sstream>
#include <iomanip>
#include <algorithm>

#define R 0.30
#define G 0.59
#define B 0.11

#define grayscale(r, g, b)(static_cast<int>(R * r + G * g + B * b))
#define minscale(r, g, b)( min(r, min(g, b)))
#define maxscale(r, g, b)( max(r, max(g, b)))
#define media(r, g, b)((r + g + b) / 3)

using namespace std;

void OUTPUT(int caso, int valor){
    cout << "Caso #" << caso << ": " << valor << endl;
}

int main(){

    int numero_casos;
    cin >> numero_casos;

    for(int i = 1; i <= numero_casos; i++){
        string tipo_conversao;
        int r, g, b, resultado;

        cin >> tipo_conversao >> r >> g >> b;

        if(tipo_conversao == "eye"){ resultado = grayscale(r, g, b); }
        if(tipo_conversao == "min"){ resultado = minscale(r, g, b); }
        if(tipo_conversao == "max"){ resultado = maxscale(r, g, b); }
        if(tipo_conversao == "mean"){ resultado = media(r, g, b); }

        OUTPUT(i, resultado);
    }
    return 0;
}