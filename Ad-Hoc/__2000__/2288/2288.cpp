#include <iostream>
#include <unordered_map>
#include <utility>
#include <vector>
#define HASH(x, y) (((x) << 16) | (y))
using namespace std;

struct Pixel {
    int value;
    int x; // linha
    int y; // coluna
};

int main() {
    int testCase = 0;
    int n, m;
    while (cin >> n >> m) {
        if (n == 0 && m == 0) break;
        unordered_map<int, Pixel> TVMatrix;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                int pixel;
                cin >> pixel;
                TVMatrix[HASH(x, y)] = {pixel, x, y};
            }
        }
        int dx, dy; // deslocamento xy
        int dxt = 0, dyt = 0; // deslocamento total xy
        while (cin >> dx >> dy) {
            if (dx == 0 && dy == 0) break;
            dxt += dx;
            dyt += dy;
        }
        for (auto& [ID, pixel] : TVMatrix) {
            // vertical
            pixel.x = ((pixel.x - dyt) % n + n) % n;
            // horizontal
            pixel.y = ((pixel.y + dxt) % m + m) % m;
        }
        vector<int> TVout(n * m);
        for (auto [id, pixel] : TVMatrix)
            TVout[pixel.x * m + pixel.y] = pixel.value;
        cout << "Teste " << ++testCase << "\n";
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                cout << TVout[x * m + y];
                if (y + 1 < m) cout << " ";
            }
            cout << "\n";
        }
        cout << "\n";
    }
}