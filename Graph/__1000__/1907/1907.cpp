#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

#define MAX 1040

char grid[MAX][MAX];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int n, m;

bool inGrid(int x, int y) {
    return x >= 1 && x <= n && y >= 0 && y < m && grid[x][y] == '.';
}

void bfs(int sx, int sy) {
    queue<pair<int, int>> q;
    q.push({sx, sy});
    grid[sx][sy] = 'o';

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (inGrid(nx, ny)) {
                grid[nx][ny] = 'o';
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    int colored_areas = 0;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; ++i)
        scanf("%s", grid[i]);

    for (int i = 1; i <= n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '.') {
                bfs(i, j);
                colored_areas++;
            }
        }
    }

    printf("%d\n", colored_areas);
    return 0;
}