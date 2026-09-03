#include <iostream>
#include <vector>
#include <utility>

using namespace std;

int main() {
    
    int n;
    while (cin >> n) {
        vector<int> v(n), p(n);
        for (int i = 0; i < n; i++) cin >> v[i];
        for (int i = 0; i < n; i++) cin >> p[i];

        int soma = 0;
        bool alterado = true;

        while (alterado) {
            alterado = false;
            for (int i = 0; i < n - 1; i++) {
                if (v[i] > v[i + 1]) {
                    soma += p[i] + p[i + 1];
                    swap(v[i], v[i + 1]);
                    swap(p[i], p[i + 1]);
                    alterado = true;
                }
            }
        }

        cout << soma << endl;
    }
    return 0;
}