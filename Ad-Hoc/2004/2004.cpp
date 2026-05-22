#include <iostream>
#include <map>
using namespace std;

int main() {
    int q;
    cin >> q;
    while(q--) {
        int n;
        cin >> n;
        map<int, int> bestValid;
        map<int, int> bestAny;
        for(int i = 0; i < n; i++) {
            int type, weight;
            cin >> type >> weight;
            bestAny[type] = max(bestAny[type], weight);
            if(weight >= 10 && weight <= 100)
                bestValid[type] = max(bestValid[type], weight);
        }
        int total = 0;
        for(auto [type, mx] : bestAny) {
            if(bestValid.count(type))
                total += bestValid[type];
            else
                total += mx;
        }
        cout << total << "\n";
    }
}