#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> fatoriais;
    fatoriais.push_back(1);

    int i = 2;

    while (fatoriais.back() <= N / i) {
        fatoriais.push_back(fatoriais.back() * i);
        i++;
    }

    int ans = 0;

    while (N != 0) {
        for (int idx = fatoriais.size() - 1; idx >= 0; idx--) {
            if (fatoriais[idx] <= N) {
                N -= fatoriais[idx];
                ans++;
                break;
            }
        }
    }

    cout << ans << '\n';

    return 0;
}