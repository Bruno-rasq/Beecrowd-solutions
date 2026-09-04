#include <iostream>
#include <unordered_set>
#include <queue>
using namespace std;

const string TARGET = "123456780";

const int DELTAS[4][2] = {{-1, 0},{1, 0},{0, -1},{0, 1}};

struct Step { string state; int moves; };

int BFS(string start) {
    queue<Step> q;
    unordered_set<string> vis;
    q.push({start, 0});
    vis.insert(start);
    while (!q.empty()) {
        Step cur = q.front();
        q.pop();
        if (cur.state == TARGET) return cur.moves;
        int zero = cur.state.find('0');
        int x = zero % 3;
        int y = zero / 3;
        for (auto [dx, dy] : DELTAS) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3) continue;
            int next = ny * 3 + nx;
            string next_state = cur.state;
            swap(next_state[zero], next_state[next]);
            if (vis.find(next_state) == vis.end()) {
                vis.insert(next_state);
                q.push({ next_state, cur.moves + 1 });
            }
        }
    }
    return -1;
}

int main() {
    string board;
    for(size_t row = 0; row < 3; row++)
        for(size_t col = 0; col < 3; col++){
            string value;
            cin >> value;
            board += value;
        }
    cout << BFS(board) << "\n";
}