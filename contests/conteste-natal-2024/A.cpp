#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(){

    int N;
    cin >> N;

    vector<int> camadas;
    for(size_t i = 0; i < N; i++){
        string estrelas;
        cin >> estrelas;
        camadas.push_back(estrelas.length());
    }

    sort(camadas.begin(), camadas.end());

    int estrelas_faltantes = 0;
    for(size_t i = camadas[0] + 2; i < camadas[N - 1]; i += 2){
        if(find(camadas.begin(), camadas.end(), i) == camadas.end()){
            cout << string(i, '*') << endl;
            estrelas_faltantes += i;
        }

    }

    cout << estrelas_faltantes << endl;
    
    return 0;
}