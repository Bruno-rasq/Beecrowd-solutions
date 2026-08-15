
#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

// A estrutura map tem como característica armazenar os valores em 
// ordem crescente, excelente para pegar os valores de distância ordenados.
// o objetivo é só garantir que os valores de tonalidade da luz também
// estejam ordenadas.
int main(){
    int N;
    cin >> N;

    int max_tonality;
    map<int, int> light_register;

    for(size_t i = 0; i < N; i++){
        int distance, tonality;
        cin >> distance >> tonality;
        light_register[distance] = tonality;
        max_tonality = max(max_tonality, tonality);
    }

    bool ans = true;
    for(const auto& [dist, tonality] : light_register){
        if(tonality > max_tonality){
            ans = false;
            break;
        }
        max_tonality = tonality;
    }

    cout << (ans ? "S" : "N") << "\n";
    return 0;
}