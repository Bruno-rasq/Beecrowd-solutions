#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

const int LIMIT = 100000;

vector<int> next_channels(int pi, const unordered_set<int>& banned_channels) {
    vector<int> adj;
    int A = pi + 1, B = pi * 2, C = pi * 3, D = pi - 1, E = pi / 2;
    if (A <= LIMIT && banned_channels.find(A) == banned_channels.end()) adj.push_back(A);
    if (B <= LIMIT && banned_channels.find(B) == banned_channels.end()) adj.push_back(B);
    if (C <= LIMIT && banned_channels.find(C) == banned_channels.end()) adj.push_back(C);
    if (D >= 1 && banned_channels.find(D) == banned_channels.end()) adj.push_back(D);
    if (pi % 2 == 0 && E >= 1 && banned_channels.find(E) == banned_channels.end()) adj.push_back(E);
    return adj;
}

int BFS(int pi, int target, const unordered_set<int>& banned_channels) {
    if (pi == target) return 0;
    vector<bool> visited(LIMIT + 1, false);
    visited[pi] = true;
    queue<pair<int, int>> q;  // (canal, cliques)
    q.push({pi, 0});

    while (!q.empty()) {
        int curr = q.front().first;
        int clicks = q.front().second;
        q.pop();

        vector<int> next_buttons = next_channels(curr, banned_channels);
        for (int next_channel : next_buttons) {
            if (next_channel == target) return clicks + 1;
            if (!visited[next_channel]) {
                visited[next_channel] = true;
                q.push({next_channel, clicks + 1});
            }
        }
    }
    return -1;  // impossível
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int O, D, K;
        cin >> O >> D >> K;
        if (O == 0 && D == 0 && K == 0) break;

        unordered_set<int> banned_channels;
        for (int i = 0; i < K; ++i) {
            int b;
            cin >> b;
            banned_channels.insert(b);
        }

        int clicks = BFS(O, D, banned_channels);
        cout << clicks << '\n';
    }
    return 0;
}