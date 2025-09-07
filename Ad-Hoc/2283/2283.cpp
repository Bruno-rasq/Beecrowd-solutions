/*

     obs: OUTPUT para c++ está com defeito na plataforma Beecrowd. erro de %5 de apresentação.

     resposta passa no kattis ICPC - final mundial de 2015
*/


#include <bits/stdc++.h>
using namespace std;
 
// Movimentos possíveis: baixo, cima, direita, esquerda
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
 
// Verifica se a posição está dentro do teclado
bool inbounds(int x, int y, int r, int c) {
    return 0 <= x && x < r && 0 <= y && y < c;
}
 
// Constrói o grafo de adjacência do teclado
vector<vector<int>> build_graph(vector<string>& grid) {
    int r = grid.size(), c = grid[0].size();
    vector<vector<int>> graph(r * c);
 
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            int cur_index = i * c + j;
            char cur_char = grid[i][j];
 
            for (int dir = 0; dir < 4; ++dir) {
                int step = 1;
                while (inbounds(i + step * dx[dir], j + step * dy[dir], r, c) &&
                       grid[i + step * dx[dir]][j + step * dy[dir]] == cur_char) {
                    step++;
                }
                int ni = i + step * dx[dir];
                int nj = j + step * dy[dir];
                if (inbounds(ni, nj, r, c)) {
                    graph[cur_index].push_back(ni * c + nj);
                }
            }
        }
    }
    return graph;
}
 
// BFS no teclado
int keyboard_bfs(vector<string>& grid, string msg) {
    int r = grid.size(), c = grid[0].size();
    msg += '*'; // marcador final
    vector<vector<int>> graph = build_graph(grid);
 
    int total_states = r * c * msg.size();
    vector<int> dist(total_states, -1);
    queue<int> q;
 
    int start_state = 0; // posição inicial (0,0), índice da mensagem 0
    dist[start_state] = 0;
    q.push(start_state);
 
    while (!q.empty()) {
        int state = q.front();
        q.pop();
 
        int pos = state % (r * c);
        int msg_index = state / (r * c);
        int x = pos / c;
        int y = pos % c;
 
        if (msg_index == msg.size() - 1) {
            return dist[state] + (msg.size() - 1);
        }
 
        // mesma tecla: digitar sem mover
        if (grid[x][y] == msg[msg_index]) {
            int next_state = state + r * c;
            if (dist[next_state] == -1) {
                dist[next_state] = dist[state];
                q.push(next_state);
            }
        }
 
        // movimentos para vizinhos
        for (int next_pos : graph[pos]) {
            int nx = next_pos / c;
            int ny = next_pos % c;
            int next_index = msg_index;
            if (grid[nx][ny] == msg[next_index]) next_index++;
            int next_state = nx * c + ny + r * c * next_index;
            if (dist[next_state] == -1) {
                dist[next_state] = dist[state] + 1;
                q.push(next_state);
            }
        }
    }
 
    return -1; // não deveria chegar aqui
}
 
int main() {
    int N, M;
    cin >> N >> M;
    cin.ignore();
 
    vector<string> keyboard(N);
    for (int i = 0; i < N; ++i) {
        getline(cin, keyboard[i]);
    }
 
    string message;
    getline(cin, message);
    message += "*";
 
    int result = keyboard_bfs(keyboard, message);
    cout << result << endl;
 
    return 0;
}