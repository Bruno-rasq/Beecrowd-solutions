#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>

using namespace std;

struct coord
{
    int x, y;
    coord(int x, int y) : x(x), y(y) {}
};

typedef vector<int> vec_t;
typedef vector<vector<int>> wall_t;
typedef vector<vector<bool>> set_t;
typedef stringstream buffet_t;

const vector<coord> deltas = {
    {-1,-1}, {-1, 0}, {-1, 1},
    {0, -1},          {0, 1},
    {1, -1},  {1, 0}, {1, 1}
};

bool inbounds(const wall_t& wall, int x, int y)
{
    return x >= 0 && x < (int)wall.size()
        && y >= 0 && y < (int)wall[0].size();
}

void wall_after_punch(wall_t& wall, coord& punch)
{
    buffet_t buffer;

    int m = wall.size();
    int n = wall[0].size();

    set_t visiteds(m, vector<bool>(n, false));
    queue<pair<coord, int>> q;

    q.push({punch, 0});
    visiteds[punch.x][punch.y] = true;
    wall[punch.x][punch.y] += 10;

    while(!q.empty())
    {
        auto [curr, dist] = q.front(); q.pop();

        int force = 10 - (dist + 1);
        if (force <= 1) continue;

        for(const auto& d : deltas)
        {
            int nx = curr.x + d.x;
            int ny = curr.y + d.y;

            if(inbounds(wall, nx, ny) && !visiteds[nx][ny])
            {
                visiteds[nx][ny] = true;
                wall[nx][ny] += force;
                q.push({coord(nx, ny), dist + 1});
            }
        }
    }

    for(int i = 0; i < m; i++)
        for(int j = 0; j < n; j++)
            if(!visiteds[i][j])
                wall[i][j] += 1;

    for(int row = 0; row < m; row++)
    {
        for(int col = 0; col < n; col++)
        {
            buffer << wall[row][col];
            if(col < n - 1) buffer << " ";
        }
        buffer << "\n";
    }

    cout << buffer.str();
}

int main()
{
    int case_number = 1;
    int amont_cases;

    cin >> amont_cases;

    for(int i = 0; i < amont_cases; i++)
    {
        cout << "Parede " << case_number << ":\n";

        int m, n, x, y;
        cin >> m >> n >> x >> y;

        wall_t wall(m, vec_t(n));
        coord punch(x - 1, y - 1);

        for(int row = 0; row < m; row++)
            for(int col = 0; col < n; col++)
                cin >> wall[row][col];

        wall_after_punch(wall, punch);
        case_number++;
    }
}