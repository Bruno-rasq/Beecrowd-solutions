#include <iostream>
#include <map>
#include <vector>
using namespace std;

using GRAPH = map<int, vector<int>>;
using HASHMAP = map<int, bool>;

/*
    Há um grafo representando tocas interligadas em vias de mão
    dupla, há N cobrinhas e 3 jogadores. um jogador está seguro
    caso não seja alcançado por uma cobra, cobras podem se mover
    livremente entre tocas interligadas.

    problema quer saber quais jogadores foram capturados e quais
    estão seguros.

    dada a posição das cobrinhas, roda uma BFS/DFS para encontrar
    todas as tocas que elas podem alcançar.
*/

void dfs(GRAPH& graph, HASHMAP& vis, int pos){
    if(vis[pos])
        return;

    vis[pos] = true;

    for(auto next : graph[pos])
        dfs(graph, vis, next);
}

int main() {

    GRAPH graph;
    HASHMAP visiteds;

    int N, M, K;
    cin >> N >> M >> K;

    for(size_t i = 0; i < N; i++){
        graph[i] = {};
        visiteds[i] = false;
    }

    // registra conexão entre toca A e B
    for(size_t i = 0; i < M; i++){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    // busca todas as tocas que cada cobra consegue alcançar
    for(size_t i = 0; i < K; i++){
        int snack_pos;
        cin >> snack_pos;
        dfs(graph, visiteds, snack_pos);
    }

    int F, B, Q;
    cin >> F >> B >> Q;

    cout << (visiteds[F] ? "PEGO" : "SEGURO") << "\n";
    cout << (visiteds[B] ? "PEGO" : "SEGURO") << "\n";
    cout << (visiteds[Q] ? "PEGO" : "SEGURO") << "\n";

    return 0;
}
