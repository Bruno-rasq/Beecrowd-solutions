#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct BIT2D {
    int n, m;
    vector<vector<int>> bit;

    BIT2D(int n, int m) : n(n), m(m), bit(n+1, vector<int>(m+1, 0)) {}

    void update(int x, int y, int val) {
        for (int i = x; i <= n; i += (i & -i)) {
            for (int j = y; j <= m; j += (j & -j)) {
                bit[i][j] += val;
            }
        }
    }

    int query(int x, int y) {
        int res = 0;
        for (int i = x; i > 0; i -= (i & -i)) {
            for (int j = y; j > 0; j -= (j & -j)) {
                res += bit[i][j];
            }
        }
        return res;
    }

    int query_rect(int x1, int y1, int x2, int y2) {
        return query(x2, y2) 
             - query(x1-1, y2) 
             - query(x2, y1-1) 
             + query(x1-1, y1-1);
    }
};

int main() {
    int N, M, C;
    while (cin >> N >> M >> C) {
        if (N == 0 && M == 0 && C == 0) break;

        BIT2D bit(N, M);
        int query;
        cin >> query;

        for (int i = 0; i < query; i++) {
            char typeQuery;
            cin >> typeQuery;

            if (typeQuery == 'A') {
                int n, x, y;
                cin >> n >> x >> y;
                bit.update(x+1, y+1, n); // 1-based
            } else {
                int x1, y1, x2, y2;
                cin >> x1 >> y1 >> x2 >> y2;
                int x_low = min(x1, x2), x_high = max(x1, x2);
                int y_low = min(y1, y2), y_high = max(y1, y2);
                cout << bit.query_rect(x_low+1, y_low+1, x_high+1, y_high+1) * C << endl;
            }
        } 
        cout << "\n";
    }
    return 0;
}