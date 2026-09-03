#include <iostream>
#include <string>
#include <utility>  // pair
#include <cmath>

using namespace std;

int main() {
    int n, m;
    while (cin >> n >> m) {
        pair<int, int> X = {-1, -1};
        pair<int, int> Y = {-1, -1};

        for (int i = 0; i < n; i++) {
            int curr;
            for (int j = 0; j < m; j++) {
                cin >> curr;
                if (curr == 1) X = make_pair(i, j);
                if (curr == 2) Y = make_pair(i, j);
            }
        }

        int dist = abs(X.first - Y.first) + abs(X.second - Y.second);
        cout << dist << endl;
        
    }

    return 0;
}