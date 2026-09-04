
#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
using namespace std;

const vector<vector<pair<int,int>>> shapes = {
    // I (2)
    {{0,0},{0,1},{0,2},{0,3}},
    {{0,0},{1,0},{2,0},{3,0}},
    // O (1)
    {{0,0},{0,1},{1,0},{1,1}},
    // S (2)
    {{0,0},{0,1},{1,1},{1,2}},
    {{0,0},{1,0},{1,-1},{2,-1}},
    // T (4)
    {{0,0},{0,1},{0,2},{1,1}},
    {{0,0},{1,0},{2,0},{1,-1}},
    {{0,0},{0,-1},{0,-2},{-1,-1}},
    {{0,0},{-1,0},{-2,0},{-1,1}},
    // L (4)
    {{0,0},{0,1},{0,2},{1,2}},
    {{0,0},{1,0},{2,0},{2,-1}},
    {{0,0},{0,-1},{0,-2},{-1,-2}},
    {{0,0},{-1,0},{-2,0},{-2,1}},
};

int main(){
    int caseTest = 1;
    while(true){
        int N;
        cin >> N;
        if(N == 0) break;
    
        vector<vector<int>> grid(N, vector<int>(N));
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                cin >> grid[i][j];

        long long ans = numeric_limits<long long>::min();
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                for(auto& shape : shapes){
                    long long sum = 0;
                    bool ok = true;
                    for(auto& [dx, dy] : shape){
                        int x = i + dx;
                        int y = j + dy;
                        if(x < 0 || x >= N || y < 0 || y >= N){
                            ok = false;
                            break;
                        }
                        sum += grid[x][y];
                    }
                    if(ok)
                        ans = max(ans, sum);
                }
            }
        }
        cout << caseTest << ". " << ans << "\n";
        caseTest++;
    }
    return 0;
}