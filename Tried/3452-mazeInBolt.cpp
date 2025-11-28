#include <bits/stdc++.h>
using namespace std;

int ROWS, COLS;

// Rotaciona a porca uma posição (direita ou esquerda)
vector<int> rotate_nut(const vector<int>& nut, const vector<char>& screw, int direction) {
    vector<int> next_nut;
    next_nut.reserve(nut.size());
    for (int idx : nut) {
        int delta = (idx + direction + COLS) % COLS;
        if (screw[delta] != '0') return {}; // bloqueado
        next_nut.push_back(delta);
    }
    return next_nut;
}

// Verifica se a porca encaixa no próximo nível do parafuso
bool check_fits(const vector<int>& nut, const vector<char>& next_screw) {
    for (int idx : nut)
        if (next_screw[idx] != '0') return false;
    return true;
}

// Faz rotações até encaixar (ou não)
vector<int> try_rotate(vector<int> spin, const vector<char>& curr_screw, const vector<char>& next_screw, int direction) {
    while (true) {
        spin = rotate_nut(spin, curr_screw, direction);
        if (spin.empty()) return {};
        if (check_fits(spin, next_screw)) return spin;
    }
}

// Tenta encaixar no próximo nível (verifica direto e depois gira)
vector<int> try_fit(vector<int> nut, const vector<char>& curr_screw, const vector<char>& next_screw) {
    if (check_fits(nut, next_screw)) return nut;

    vector<int> spin_left = try_rotate(nut, curr_screw, next_screw, -1);
    if (!spin_left.empty()) return spin_left;

    vector<int> spin_right = try_rotate(nut, curr_screw, next_screw, 1);
    if (!spin_right.empty()) return spin_right;

    return {};
}

// Valida se a porca consegue descer o labirinto
bool validate_nut_and_mazebolt(const vector<vector<char>>& MAZE, vector<int> nut, vector<char> current_screw) {
    for (int i = 0; i < ROWS; ++i) {
        nut = try_fit(nut, current_screw, MAZE[i]);
        if (nut.empty()) return false;
        current_screw = MAZE[i];
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> ROWS >> COLS;

    string nut_str;
    cin >> nut_str;

    vector<int> nut;
    for (int i = 0; i < COLS; ++i)
        if (nut_str[i] == '1') nut.push_back(i);

    vector<vector<char>> MAZE(ROWS, vector<char>(COLS));
    for (int i = 0; i < ROWS; ++i) {
        string row;
        cin >> row;
        for (int j = 0; j < COLS; ++j)
            MAZE[i][j] = row[j];
    }

    vector<char> current_screw(COLS, '0');

    bool ok = validate_nut_and_mazebolt(MAZE, nut, current_screw);
    cout << (ok ? "Y\n" : "N\n");
    return 0;
}