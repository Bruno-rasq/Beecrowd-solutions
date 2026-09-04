#include <iostream>
#include <vector>
#include <utility>
#include <cmath>

using namespace std;

int dominant_bishops(int n, vector<pair<int, int>>& bishops) {
    int dominates = 0;

    for (int i = 0; i < n; i++) {
        int xa = bishops[i].first;
        int ya = bishops[i].second;
        bool dominant = true;

        for (int j = 0; j < n; j++) {
            if (i == j) continue;

            int xb = bishops[j].first;
            int yb = bishops[j].second;

            if (abs(xa - xb) == abs(ya - yb)) {
                dominant = false;
                break;
            }
        }

        if (dominant) dominates++;
    }

    return dominates;
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> bishops(n);
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;
        bishops[i] = make_pair(x, y);
    }

    int out = dominant_bishops(n, bishops);
    cout << out << endl;

    return 0;
}