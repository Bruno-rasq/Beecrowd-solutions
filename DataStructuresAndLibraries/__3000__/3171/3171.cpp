#include <iostream>
#include <map>
#include <vector>
#include <set>

using namespace std;

void DFS(set<int> visitados, map<int, vector<int>> grafico, int node){
    visitados.insert(node);
    for(const int& visinho: grafico[node]){
        DFS(visitados, grafico, visinho);
    }
}

int main(){

    int n_leds, n_segmentos;
    while(cin >> n_leds >> n_segmentos){

        map<int, vector<int>> grafico;
        set<int> visitados;

        for(int i = 0; i < n_segmentos; i++){
            int N, M;
            cin >> N >> M;

            if(grafico.find(N) == grafico.end()) grafico[N] = vector<int>();
            if(grafico.find(M) == grafico.end()) grafico[M] = vector<int>();

            grafico[N].push_back(M);
            grafico[M].push_back(N);
        }

        DFS(visitados, grafico, 1);

        cout << (n_leds == visitados.size() ? "COMPLETO" : "INCOMPLETO") << endl;
    }

    return 0;
}