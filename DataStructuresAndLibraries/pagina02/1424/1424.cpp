#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    int n, m, curr, key, ind;

    while (cin >> n >> m) {
        unordered_map<int, vector<int>> ocorrencias;

        for (int i = 0; i < n; i++) {
            cin >> curr;
            ocorrencias[curr].push_back(i + 1); // 1-indexado
        }

        for (int i = 0; i < m; i++) {
            cin >> ind >> key;  // CORREÇÃO: ordem correta (k, v)
            if (ocorrencias.find(key) != ocorrencias.end() &&
                ocorrencias[key].size() >= ind) {
                cout << ocorrencias[key][ind - 1] << endl;
            } else {
                cout << 0 << endl;
            }
        }
    }

    return 0;
}