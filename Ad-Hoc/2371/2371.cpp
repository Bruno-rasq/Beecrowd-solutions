#include <bits/stdc++.h>
using namespace std;

const int DELTA[4][2] = {{-1, 0},{ 1, 0},{ 0,-1},{ 0, 1}};

int main() {
    
    int N, M;
    cin >> N >> M;
    vector<string> board(N + 1);
    for(int i = 1; i <= N; i++) {
        string row;
        cin >> row;
        board[i] = " " + row;
    }

    vector<vector<int>> shipId(N + 1, vector<int>(M + 1, -1));
    vector<int> remaining;
    int currentId = 0;
    for(int row = 1; row <= N; row++) {
        for(int col = 1; col <= M; col++) {
            if(board[row][col] != '#' || shipId[row][col] != -1)
                continue;

            remaining.push_back(0);

            queue<pair<int,int>> q;
            q.push({row, col});
            shipId[row][col] = currentId;

            while(!q.empty()) {
                auto [x, y] = q.front();
                q.pop();

                remaining[currentId]++;

                for(auto &d : DELTA) {
                    int nx = x + d[0];
                    int ny = y + d[1];

                    if(nx < 1 || nx > N || ny < 1 || ny > M) continue;
                    if(board[nx][ny] != '#') continue;
                    if(shipId[nx][ny] != -1) continue;

                    shipId[nx][ny] = currentId;
                    q.push({nx, ny});
                }
            }

            currentId++;
        }
    }

    vector<vector<bool>> hit(N + 1, vector<bool>(M + 1, false));
    int K;
    cin >> K;
    int destroyed = 0;
    while(K--) {
        int L, C;
        cin >> L >> C;
        if(shipId[L][C] == -1) continue;
        if(hit[L][C]) continue;
        hit[L][C] = true;
        int id = shipId[L][C];
        remaining[id]--;
        if(remaining[id] == 0) destroyed++;
    }

    cout << destroyed << '\n';
    return 0;
}