#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// ENCONTRAR A MENOR QUANTIDADE DE MOVIMENTOS PARA MOVER UM CAVALO DE
// UMA POSIÇÃO NO TABULEIRO DE XADREZ ATÉ OUTRA POSIÇÃO. PORÉM O JOGO
// É UMA VARIANTE 3D (MAIS NIVEIS DE TABULEIROS EM UM EIXO Z).

struct POSITION {
    int x;        // INDICE DA LINHA.
    int y;        // INDICE DA COLUNA.
    int z;        // NIVEL DO TABULEIRO.
};

struct STEP {
    int moves;    // QUANTIDADE DE MOVIMENTOS FEITOS.
    POSITION pos;
};

// TODAS AS CÉLULAS ADJACENTES DADA UMA POSIÇÃO DO CAVALO NO TABULEIRO.
const vector<POSITION> ADJACENTS = {
    { 0, 1, 2}, { 0, 1,-2},
    { 0,-1, 2}, { 0,-1,-2},
    { 0, 2, 1}, { 0, 2,-1},
    { 0,-2, 1}, { 0,-2,-1},
    { 1, 0, 2}, { 1, 0,-2},
    {-1, 0, 2}, {-1, 0,-2},
    { 1, 2, 0}, { 1,-2, 0},
    {-1, 2, 0}, {-1,-2, 0},
    { 2, 0, 1}, { 2, 0,-1},
    {-2, 0, 1}, {-2, 0,-1},
    { 2, 1, 0}, { 2,-1, 0},
    {-2, 1, 0}, {-2,-1, 0}
};

// BUSCA TODO AS CELULAS DO TABULEIRO POR POSIÇÕES ADJACENTES (POSSIBILIDADES)
// EM CAMADAS E NIVEIS AFIM DE CHEGAR NA POSIÇÃO DESEJADA, RETORNA A QUANTIDADE DE AÇÕES.
int BFS(const int R, const int C, const int N, const POSITION& source, const POSITION& target){
    if(source.x == target.x && source.y == target.y && source.z == target.z)
        return 0;

    vector<vector<vector<bool>>> visited(R, vector<vector<bool>>(C, vector<bool>(N, false)));
    queue<STEP> Q;

    Q.push({0, source});
    visited[source.x][source.y][source.z] = true;

    while(!Q.empty()){
        STEP curr = Q.front();
        Q.pop();

        if(curr.pos.x == target.x && curr.pos.y == target.y && curr.pos.z == target.z)
            return curr.moves;

        for(const POSITION& adj : ADJACENTS){
            int nx = curr.pos.x + adj.x;
            int ny = curr.pos.y + adj.y;
            int nz = curr.pos.z + adj.z;
            if(nx >= 0 && nx < R && ny >= 0 && ny < C && nz >= 0 && nz < N){
                if(!visited[nx][ny][nz]){
                    visited[nx][ny][nz] = true;
                    Q.push({curr.moves + 1, {nx, ny, nz}});
                }
            }
        }
    }
    return -1;
}

int main() {
    // Otimização de I/O para C++
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int R, C, N, xi, yi, zi, xf, yf, zf;
    if (cin >> R >> C >> N >> xi >> yi >> zi >> xf >> yf >> zf) {
        // Correção do erro de 15%: Convertendo a entrada (base-1) para índices de matriz (base-0)
        xi--; yi--; zi--;
        xf--; yf--; zf--;
        
        cout << BFS(R, C, N, {xi, yi, zi}, {xf, yf, zf}) << "\n";
    }
    return 0;
}
