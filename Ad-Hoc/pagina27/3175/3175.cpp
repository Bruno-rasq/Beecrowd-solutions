#include <iostream>
#include <set>         // armazena valores unicos de forma ordenada.
#include <vector>
#include <unordered_map>
#include <cstdint>
using namespace std;

int main() {
    int N;
    cin >> N;
    set<int> uniques;
    vector<int> gooddeeds(N, 0);
    for(size_t i = 0; i < N; i++){
        cin >> gooddeeds[i];
        uniques.insert(gooddeeds[i]);
    }

    unordered_map<uint, int> gift;
    int rank = 1;
    for (int x : uniques) {
        gift[x] = rank++;
    }

    uint64_t ans = 0;
    for(size_t i = 0; i < N; i++){
        int value = gooddeeds[i];
        int qnt_presents = gift[value];
        ans += qnt_presents;
    }

    cout << ans << "\n";
}