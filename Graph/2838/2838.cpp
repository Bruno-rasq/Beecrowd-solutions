#include <bits/stdc++.h>
using namespace std;

// estados da bfs carregam informações relevantes em inteiros.
struct State { int x, y, keys, gems, steps;};

const int ALLGEMSCOLLECTED = 31; // (11111)
const int DELTAS[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
const unordered_map<char, int> GEMS = {{'p', 5}, {'t', 4}, {'m', 3}, {'e', 2}, {'r', 1}};

// SET: ativa o bit referente a chave/gema coletada
void SET(int& collection, int idx){ collection |= (1 << (idx - 1));}

// QUERY: verifica se o bit está ativo.
bool QUERY(const int& collection, int idx){ return collection & (1 << (idx - 1));}

// criar uma string unica para cada estado.
string StringfyState(int x, int y, int keys, int gems){
    ostringstream oss;
    oss << x << "-" << y << "-" << keys << "-" << gems;
    return oss.str();
}

int BFS(vector<string>& board, int x, int y, int n, int m){

    queue<State> q;
    unordered_set<string> vis;
    q.push({x, y, 0, 0, 0});
    vis.insert(StringfyState(x, y, 0, 0));

    while(!q.empty()){
        State curr = q.front();
        q.pop();

        if(curr.gems == ALLGEMSCOLLECTED) return curr.steps;

        for(const auto& delta : DELTAS){
            int nx = curr.x + delta[0];
            int ny = curr.y + delta[1];

            if(nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

            char cell = board[nx][ny];

            if(cell == '#') continue;

            // portas trancadas
            if(cell == 'A' && !QUERY(curr.keys, 4)) continue;
            if(cell == 'B' && !QUERY(curr.keys, 3)) continue;
            if(cell == 'C' && !QUERY(curr.keys, 2)) continue;
            if(cell == 'D' && !QUERY(curr.keys, 1)) continue;

            int nextKeys = curr.keys;
            int nextGems = curr.gems;

            // encontrou uma chave
            if(cell == 'a') SET(nextKeys, 4);
            if(cell == 'b') SET(nextKeys, 3);
            if(cell == 'c') SET(nextKeys, 2);
            if(cell == 'd') SET(nextKeys, 1);

            // encontrou uma gema
            auto it = GEMS.find(cell);
            if(it != GEMS.end()) SET(nextGems, it->second);

            string nextState = StringfyState(nx, ny, nextKeys, nextGems);
            if(vis.count(nextState)) continue;
            vis.insert(nextState);

            q.push({nx, ny, nextKeys, nextGems, curr.steps + 1});
        }
    }
    return -1;
}

int main(){
    int n, m;
    cin >> n >> m;
    cin.ignore();
    int x = 0, y = 0;
    vector<string> board(n);
    for(int i = 0; i < n; i++){
        getline(cin, board[i]);
        for(int j = 0; j < m; j++){
            if(board[i][j] == 'T'){
                x = i;
                y = j;
            }
        }
    }
    int ans = BFS(board, x, y, n, m);
    if(ans == -1) cout << "Gamora\n";
    else cout << ans << "\n";
}