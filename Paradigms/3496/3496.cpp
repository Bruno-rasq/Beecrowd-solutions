#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> tshirts;
    tshirts.assign(n, 0);
    for(size_t i = 0; i < n; i++)
        cin >> tshirts[i];
    sort(tshirts.begin(), tshirts.end());
    long long cost = 0;
    for(long long i = n - 1; i >= 0; i -= 2)
        cost += tshirts[i];
    cout << cost << "\n";
    return 0;
}
