#include <bits/stdc++.h>
using namespace std;

/**
 *  Ideia de solução:
 *  Ponto 3D -> aresta -> hashmap -> grafo -> bfs
*/

struct Point {
    int x, y, z;
    bool operator==(const Point& other) const {
        return x == other.x && y == other.y && z == other.z;
    }
    bool operator<(const Point& other) const {
        if (x != other.x) return x < other.x;
        if (y != other.y) return y < other.y;
        return z < other.z;
    }
};

struct Edge {
    Point a, b;
    Edge(Point p1, Point p2) {
        if (p2 < p1) swap(p1, p2); // normaliza
        a = p1;
        b = p2;
    }
    bool operator==(const Edge& other) const {
        return a == other.a && b == other.b;
    }
};

struct EdgeHash {
    size_t operator()(const Edge& e) const {
        size_t h = 0;
        auto mix = [&](int v) {
            h ^= hash<int>()(v) + 0x9e3779b9 + (h << 6) + (h >> 2);
        };
        mix(e.a.x); mix(e.a.y); mix(e.a.z);
        mix(e.b.x); mix(e.b.y); mix(e.b.z);
        return h;
    }
};

using EDGEMAP = unordered_map<Edge, vector<int>, EdgeHash>;

EDGEMAP buildEdgeMapFromInput(int c) {
    EDGEMAP edge_map;
    for (int cityID = 0; cityID < c; cityID++) {
        int n;
        cin >> n;
        vector<Point> poly(n);
        for (int i = 0; i < n; i++) {
            cin >> poly[i].x >> poly[i].y >> poly[i].z;
        }
        for (int i = 0; i < n; i++) {
            Point p1 = poly[i];
            Point p2 = poly[(i + 1) % n];
            Edge e(p1, p2);
            edge_map[e].push_back(cityID);
        }
    }
    return edge_map;
}

vector<vector<int>> buildGraph(const EDGEMAP& edge_map, int c) {
    vector<vector<int>> adj(c);
    for (const auto& [edge, countries] : edge_map) {
        if (countries.size() == 2) {
            int u = countries[0];
            int v = countries[1];
            if (u != v) { // segurança extra
                adj[u].push_back(v);
                adj[v].push_back(u);
            }
        }
    }
    return adj;
}

int bfs(const vector<vector<int>>& adj, int start, int target) {
    vector<int> dist(adj.size(), -1);
    queue<int> q;
    dist[start] = 0;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (u == target) return dist[u];
        for (int v : adj[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    return -1; // não deve acontecer
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    while (true) {
        int c;
        cin >> c;
        if (c == 0) break;
        auto edge_map = buildEdgeMapFromInput(c);
        auto graph = buildGraph(edge_map, c);
        int m;
        cin >> m;
        while (m--) {
            int a, b;
            cin >> a >> b;
            // converter 1-based → 0-based
            a--; 
            b--;
            cout << bfs(graph, a, b) << '\n';
        }
    }
    return 0;
}