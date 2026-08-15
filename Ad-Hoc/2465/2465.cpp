#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

typedef unordered_set<uint32_t> s_t;

const vector<vector<int>> DELTA_MOVE = {
    {0, 1},   // DIREITA
    {1, 0},   // BAIXO
    {0, -1},  // ESQUERDA
    {-1, 0}   // CIMA
};

void dfs(vector<vector<int>>& board, int& ans, s_t& VISITEDS, int x, int y){

    // Recebeu a bola -> levanta a bandeira
    uint32_t curr_packet = (y << 8) | x;

    VISITEDS.insert(curr_packet);
    ans++;

    // Executa as 4 rotações
    for(const auto& delta : DELTA_MOVE){

        int dx = delta[0];
        int dy = delta[1];

        int nx = x + dx;
        int ny = y + dy;

        // Está fora da matriz
        if(nx < 0 || nx >= board.size() ||
           ny < 0 || ny >= board.size())
            continue;

        // Número do colega é menor
        if(board[nx][ny] < board[x][y])
            continue;

        uint32_t next_packet = (ny << 8) | nx;

        // A bandeira dele já está levantada
        if(VISITEDS.find(next_packet) != VISITEDS.end())
            continue;

        // Passa a bola e espera ela voltar
        dfs(board, ans, VISITEDS, nx, ny);

        // A bola voltou.
        // Continua para a próxima direção.
    }
}

int main(){

    int grid_size;
    int x, y;

    cin >> grid_size;
    cin >> x >> y;

    // A entrada começa em 1
    // Nosso vetor começa em 0
    x--;
    y--;

    vector<vector<int>> board(
        grid_size,
        vector<int>(grid_size)
    );

    for(int i = 0; i < grid_size; i++)
        for(int j = 0; j < grid_size; j++)
            cin >> board[i][j];

    int ans = 0;

    s_t VISITEDS;

    dfs(board, ans, VISITEDS, x, y);

    cout << ans << '\n';

    return 0;
}