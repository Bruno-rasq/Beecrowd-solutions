#include <iostream>
#include <queue>
#include <sstream>
#include <vector>
#include <utility>
using namespace std;

// RESCREVER UM PROGRAMA QUE SIMULE A FERRAMENTA PREENCHER DO PAINT
// DADA UM FRAME, UMA COORDENADA XY E UMA COR, EXIBA O ESTADO DO FRAME
// APÓS O PREENCHIMENTO.

#define FRAME vector<vector<int>>
#define QUEUE queue<pair<int, int>>


void FILL(FRAME& FR, QUEUE& Q, int x, int y, int color, int old_color){
    if(x >= 0 && x < FR.size() && y >= 0 && y < FR[0].size() && FR[x][y] == old_color){
        FR[x][y] = color;
        Q.push({x, y});
    }
}


int main() {

    int N, M;
    while(cin >> N >> M){

        int x, y, color;
        FRAME FR(N, vector<int>(M, 0));

        for(size_t i = 0; i < N; i++)
            for(size_t j = 0; j < M; j++)
                cin >> FR[i][j];

        cin >> x >> y >> color;
        x--;
        y--;

        int old_color = FR[x][y];

        if(old_color != color){

            QUEUE Q;
            FR[x][y] = color;
            Q.push({x, y});

            while(!Q.empty()){
                pair<int, int> curr = Q.front();
                Q.pop();

                FILL(FR, Q, curr.first - 1, curr.second, color, old_color);
                FILL(FR, Q, curr.first, curr.second + 1, color, old_color);
                FILL(FR, Q, curr.first + 1, curr.second, color, old_color);
                FILL(FR, Q, curr.first, curr.second - 1, color, old_color);
            }
        }

        stringstream buffer;
        for(size_t i = 0; i < N; i++){
            buffer << FR[i][0];
            for(size_t j = 1; j < M; j++){
                buffer << " " << FR[i][j];
            }
            buffer << "\n";
        }
        cout << buffer.str();
    }
    return 0;
}