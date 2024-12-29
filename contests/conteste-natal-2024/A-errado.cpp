#include <iostream>
#include <vector>

using namespace std;

int main(){

    int N;
    cin >> N;

    vector<int> camadas(N);
    for(size_t i = 0; i < N; i++){
        string estrelas;
        cin >> estrelas;
        camadas.push_back(estrelas);
    }

    int totalEstrelas = 0;
    for(size_t i = camadas[0] + 2; i < camadas[N - 1]; i += 2){
        cout << string(i, "*") << endl;
        totalEstrelas++;
    }

    int estrelasFaltantes = totalEstrelas - (camadas[0] - camadas[N - 1]);
    cout << estrelasFaltantes << endl;
    
    return 0;
}