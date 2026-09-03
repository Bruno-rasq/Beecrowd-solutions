#include <iostream>
#include <vector>
#include <camth>
using namespace std;

float calcularArea(vector<pair<int, int>>& pontos){
    int n = pontos.size();
    float soma1 = 0, soma2 = 0;

    for (int i = 0; i < n; i++){
        int x1 = pontos[i].first;
        int y1 = pontos[i].second;
        int x2 = pontos[(i + 1) % n].first;
        int y2 = pontos[(i + 1) % n].second;

        soma1 += x1 * y2;
        soma2 += y1 * x2;
    }

    return abs(soma1 - soma2) / 2.0;
}

int main(){

    vector<pair<int, int>> terrenoA(4);
    vector<pair<int, int>> terrenoB(4);

    for(int i = 0; i < 4; i++){
        cin >> terrenoA[i].first >> terrenoA[i].second;
    }
    for(int i = 0; i < 4; i++){
        cin >> terrenoB[i].first >> terrenoB[i].second;
    }

    float areaA = calcularArea(terrenoA);
    float areaB = calcularArea(terrenoB);

    cout << (areaA > areaB) ? areaA : areaB << endl;

    return 0;
}