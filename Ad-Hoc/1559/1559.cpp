#include <iostream>
#include <array>
#include <string>

using namespace std;

// Trata todas as linhas independente do sentido do movimento como se fosse da esquerda para 
// direita. Isso simplifica o código evitando reescrever a função para os 4 sentidos.
bool is_possible_to_move(const array<int, 4>& row) {
    for (size_t i = 0; i < 3; i++) {
        size_t j = i + 1;

        bool left_cell_is_zero = row[i] == 0 && row[j] != 0;
        bool left_right_cell_equals = row[i] == row[j];

        if (left_cell_is_zero || (left_right_cell_equals && row[i] != 0))
            return true;
    }
    return false;
}

string all_possible_moves(const array<array<int, 4>, 4>& g) {
    bool left = false, down = false, up = false, right = false;

    const array<array<int, 4>, 16> rows = {
        // Left / Right
        array<int,4>{g[0][0], g[0][1], g[0][2], g[0][3]}, array<int,4>{g[0][3], g[0][2], g[0][1], g[0][0]},
        array<int,4>{g[1][0], g[1][1], g[1][2], g[1][3]}, array<int,4>{g[1][3], g[1][2], g[1][1], g[1][0]},
        array<int,4>{g[2][0], g[2][1], g[2][2], g[2][3]}, array<int,4>{g[2][3], g[2][2], g[2][1], g[2][0]},
        array<int,4>{g[3][0], g[3][1], g[3][2], g[3][3]}, array<int,4>{g[3][3], g[3][2], g[3][1], g[3][0]},

        // Up / Down
        array<int,4>{g[0][0], g[1][0], g[2][0], g[3][0]}, array<int,4>{g[3][0], g[2][0], g[1][0], g[0][0]},
        array<int,4>{g[0][1], g[1][1], g[2][1], g[3][1]}, array<int,4>{g[3][1], g[2][1], g[1][1], g[0][1]},
        array<int,4>{g[0][2], g[1][2], g[2][2], g[3][2]}, array<int,4>{g[3][2], g[2][2], g[1][2], g[0][2]},
        array<int,4>{g[0][3], g[1][3], g[2][3], g[3][3]}, array<int,4>{g[3][3], g[2][3], g[1][3], g[0][3]}
    };

    for (size_t i = 0; i < 8; i += 2) {
        if (is_possible_to_move(rows[i]))     left  = true;
        if (is_possible_to_move(rows[i + 1])) right = true;
    }
    
    for (size_t i = 8; i < 16; i += 2) {
        if (is_possible_to_move(rows[i]))     up   = true;
        if (is_possible_to_move(rows[i + 1])) down = true;
    }

    string out = "";
    out += (down  ? (out != "" ? " DOWN"  : "DOWN") : "");
    out += (left  ? (out != "" ? " LEFT"  : "LEFT") : "");
    out += (right ? (out != "" ? " RIGHT" : "RIGHT") : "");
    out += (up    ? (out != "" ? " UP"    : "UP")   : "");

    return (out == "") ? "NONE" : out;
}

int main() {
    int n, curr;
    cin >> n;

    for (size_t test_case = 0; test_case < n; test_case++) {
        array<array<int, 4>, 4> grid = {0};
        bool is_end = false;

        for (size_t i = 0; i < 4; i++) {
            for (size_t j = 0; j < 4; j++) {
                cin >> curr;
                grid[i][j] = curr;
                if (curr == 2048) is_end = true;
            }
        }

        cout << (is_end ? "NONE" : all_possible_moves(grid)) << endl;
    }

    return 0;
}