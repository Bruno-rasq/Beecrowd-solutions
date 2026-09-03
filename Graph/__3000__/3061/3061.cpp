#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Coord { int x, y; };

const vector<Coord> DELTAS = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

// a bfs vai percorrer todas as celulas validas e marcar-las como visitadas.
void MarkVisitedCells(vector<vector<int>>& grid, Coord start){
    queue<Coord> q;
    q.push(start);
    grid[start.x][start.y] = 0;   // marca a origem
    while(!q.empty()){
        Coord curr = q.front();
        q.pop();
        for(auto& delta : DELTAS){
            int nx = curr.x + delta.x;
            int ny = curr.y + delta.y;
            if(nx >= 0 && nx < grid.size() &&
               ny >= 0 && ny < grid[0].size() &&
               grid[nx][ny] == 1){

                grid[nx][ny] = 0;
                q.push({nx, ny});
            }
        }
    }
}

int main() {
    int x, y;
    cin >> x >> y;

    vector<vector<int>> grid;
    for(size_t i = 0; i < x; i++){
        vector<int> row(y, 0);
        for(size_t j = 0; j < y; j++){
            cin >> row[j];
        }
        grid.push_back(row);
    }

    int blemishes = 0;
    for(int i = 0; i < x; i++){
        for(int j = 0; j < y; j++){
            if(grid[i][j] == 1){
                blemishes++;
                MarkVisitedCells(grid, {i, j});
            }
        }
    }

    cout << blemishes << "\n";
}