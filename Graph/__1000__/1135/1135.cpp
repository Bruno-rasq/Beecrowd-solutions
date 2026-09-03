#include <bits/stdc++.h>
using namespace std;

class AntsColony {
public:
    static long long shortestPathBetween(
        const vector<pair<int,long long>>& gp,
        const vector<int>& depth, int p, int q) {
        
        long long custo = 0;
        int dp = depth[p];
        int dq = depth[q];
        
        while (dp > dq) {
            custo += gp[p].second;
            p = gp[p].first;
            dp--;
        }
        while (dq > dp) {
            custo += gp[q].second;
            q = gp[q].first;
            dq--;
        }
        
        while (p != q) {
            custo += gp[p].second + gp[q].second;
            p = gp[p].first;
            q = gp[q].first;
        }
        
        return custo;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    while (true) {
        int vertices;
        cin >> vertices;
        if (vertices == 0) break;
        
        vector<pair<int,long long>> gp(vertices);
        vector<int> depth(vertices);
        
        gp[0] = {0, 0LL};
        depth[0] = 0;
        
        for (int i = 1; i < vertices; i++) {
            int parent;
            long long weight;
            cin >> parent >> weight;
            gp[i] = {parent, weight};
            depth[i] = depth[parent] + 1;
        }
        
        int queries;
        cin >> queries;
        for (int i = 0; i < queries; i++) {
            int p, q;
            cin >> p >> q;
            if (i > 0) cout << " ";
            cout << AntsColony::shortestPathBetween(gp, depth, p, q);
        }
        cout << "\n";
    }
    
    return 0;
}