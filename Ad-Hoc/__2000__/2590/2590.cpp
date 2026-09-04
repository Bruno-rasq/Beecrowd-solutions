#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    static const int cycle[4] = {7, 9, 3, 1};  // ciclo fixo
    
    while (n--) {
        long long k;
        cin >> k;
        cout << cycle[(k - 1) % 4] << '\n';  // pega direto do ciclo
    }
    
    return 0;
}