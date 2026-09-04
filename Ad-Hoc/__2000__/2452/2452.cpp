#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Step { int idx, step; };

int main() {
    int F, R;
    cin >> F >> R;

    queue<Step> q;
    vector<bool> visited(F, false); // mais rápido que set

    for (int i = 0; i < R; i++) {
        int pos;
        cin >> pos;
        pos--; // converter para 0-based

        q.push({pos, 0});
        visited[pos] = true;
    }

    int days = 0;
    int deltas[2] = {-1, 1};

    while (!q.empty()) {
        Step cur = q.front();
        q.pop();

        for (int dx : deltas) {
            int nx = cur.idx + dx;

            if (nx >= 0 && nx < F && !visited[nx]) {
                visited[nx] = true;
                q.push({nx, cur.step + 1});
                days = max(days, cur.step + 1);
            }
        }
    }

    cout << days << endl;
    return 0;
}