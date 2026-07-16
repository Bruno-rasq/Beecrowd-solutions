#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
    int n, h, l;
    cin >> n >> h >> l;

    vector<int> horror_list(h);
    for (int i = 0; i < h; i++)
        cin >> horror_list[i];

    vector<vector<int>> graph(n);
    const int INF = 1e9;
    vector<int> dist(n, INF);
    for (int i = 0; i < l; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    queue<int> fila;
    for (int x : horror_list) {
        dist[x] = 0;
        fila.push(x);
    }

    while (!fila.empty()) {
        int curr = fila.front();
        fila.pop();
        for (int v : graph[curr]) {
            if (dist[v] == INF) {
                dist[v] = dist[curr] + 1;
                fila.push(v);
            }
        }
    }

    int maxH = dist[0];
    for (int i = 1; i < n; i++)
        maxH = max(maxH, dist[i]);

    for (int i = 0; i < n; i++) {
        if (dist[i] == maxH) {
            cout << i << '\n';
            break;
        }
    }
    return 0;
}