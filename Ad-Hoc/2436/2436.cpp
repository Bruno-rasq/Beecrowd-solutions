#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> MATRIX;
typedef pair<int, int> COORD;
typedef vector<pair<int, int>> Deltas;

const Deltas DELTA = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}}; // esquerda, direita, baixo, cima

COORD move(MATRIX& Board, int pos_x, int pos_y) {
    for (auto [dx, dy] : DELTA) {
        int nx = pos_x + dx;
        int ny = pos_y + dy;
        if (nx >= 0 && nx < (int)Board.size() &&
            ny >= 0 && ny < (int)Board[0].size() &&
            Board[nx][ny] == 1) {
            return {nx, ny};
        }
    }
    return {-1, -1}; // sem vizinho preto
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int L, C, A, B;
    cin >> L >> C >> A >> B;

    MATRIX board(L, vector<int>(C));
    for (int i = 0; i < L; i++)
        for (int j = 0; j < C; j++)
            cin >> board[i][j];

    int x = A - 1;
    int y = B - 1;

    // 🚩 Igual ao Python: já marca o ponto inicial como visitado
    board[x][y] = 0;

    while (true) {
        auto [nx, ny] = move(board, x, y);
        if (nx == -1) break;
        board[nx][ny] = 0; // marca visitado
        x = nx;
        y = ny;
    }

    cout << (x + 1) << " " << (y + 1) << "\n";
}