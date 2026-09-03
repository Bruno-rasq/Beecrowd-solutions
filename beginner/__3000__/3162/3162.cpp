#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int pow(int n){ return n * n; }

double calcDistancia(vector<int> nave_atual, vector<int> nave_proxima){
    int c1x = nave_atual[0], c1y = nave_atual[1], c1z = nave_atual[2];
    int c2x = nave_proxima[0], c2y = nave_proxima[1], c2z = nave_proxima[2];

    return sqrt(
        pow(c2x - c1x) + pow(c2y - c1y) + pow(c2z - c1z)
    );
}

int main(){

    int numero_naves;
    cin >> numero_naves;

    vector<vector<int>> naves;

    for(int i = 0; i < numero_naves; i++){
        int x, y, z;
        cin >> x >> y >> z;
        naves.push_back({x, y, z});
    }

    for(int i = 0; i < numero_naves; i++){
        vector<int> nave_atual = naves[i];
        double menor_distancia = INFINITY;

        for(int j = 0; j < numero_naves; j++){
            if(j != i){
                vector<int> nave_proxima = naves[j];
                double distancia = calcDistancia(nave_atual, nave_proxima);

                if(menor_distancia < distancia){ menor_distancia = distancia; } 
            }
        }

        if(menor_distancia > 50){ cout << "B" << endl; }
        else if (menor_distancia <= 50 && menor_distancia > 20){ cout << "M" << endl; }
        else { cout << "A" << endl;}
        
    }
    return 0;
}