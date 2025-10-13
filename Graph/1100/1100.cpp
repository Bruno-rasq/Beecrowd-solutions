#include <iostream>
#include <vector>
#include <utility>
#include <tuple>
#include <string>
#include <unordered_set>
#include <queue>
#include <sstream>

using namespace std;

// Definindo um tipo para coordenadas
using TCoord = pair<int, int>;

// Hash para usar pair<int,int> em unordered_set
struct PairHash {
    size_t operator()(const TCoord& coord) const {
        return hash<int>()(coord.first) ^ (hash<int>()(coord.second) << 1);
    }
};

typedef unordered_set<TCoord, PairHash> HashSet;
typedef pair<int, TCoord> Moves;  // número de movimentos + coordenada

// variações de coordenadas para cada salto do cavalo
const vector<pair<int, int>> DELTA = {
    { 2,  1}, { 1,  2}, {-1,  2}, {-2,  1},
    {-2, -1}, {-1, -2}, { 1, -2}, { 2, -1}
};

// checa se as coordenadas x, y estão dentro do limite do board
bool inBound(int x, int y) {
    return 0 <= x && x < 8 && 0 <= y && y < 8;
}

// Transforma a posição (ex: "a1") em coordenadas (linha, coluna)
TCoord GetCoord(const string& position) {
    int col = position[0] - 'a'; // 'a' → 0, 'b' → 1, ...
    int row = position[1] - '1'; // '1' → 0, '2' → 1, ...
    return {row, col};
}

// Breadth_First_Search - BFS 
int BFS(const TCoord& source, const TCoord& target) {
    
    HashSet visiteds;                      // set das coordenadas visitadas
    queue<Moves> q;                        // fila de jogadas

    q.push({0, source});                   // adiciona primeira jogada (0 movimentos, coord inicial)
    visiteds.insert(source);               // marca coord inicial como visitada

    while (!q.empty()) {
        Moves move = q.front();
        q.pop();

        int moves = move.first;
        int x = move.second.first;
        int y = move.second.second;

        if (move.second == target) return moves; // chegou no alvo

        for (auto [dx, dy] : DELTA) {            // testa cada uma das jogadas possíveis
            int nx = x + dx;
            int ny = y + dy;

            TCoord next = {nx, ny};

            if (inBound(nx, ny) && visiteds.find(next) == visiteds.end()) {
                visiteds.insert(next);
                q.push({moves + 1, next});
            }
        }
    }

    return -1; // só por garantia.
}

int main() {
    string source, target;
    while (cin >> source >> target) {
        TCoord source_coord = GetCoord(source);
        TCoord target_coord = GetCoord(target);

        int moves = BFS(source_coord, target_coord);

        cout << "To get from " << source << " to " << target
             << " takes " << moves << " knight moves." << endl;
    }
    return 0;
}