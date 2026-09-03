#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N, M;
        cin >> N >> M;
        vector<int> blocks(N);
        for (int i = 0; i < N; i++) {
            cin >> blocks[i];
        }

        vector<int> dp(M + 1, INT_MAX);
        dp[0] = 0;

        for (int i = 1; i <= M; i++) {
            for (int j = 0; j < N; j++) {
                if (i >= blocks[j] && dp[i - blocks[j]] != INT_MAX) {
                    dp[i] = min(dp[i], dp[i - blocks[j]] + 1);
                }
            }
        }

        cout << dp[M] << "\n";
    }
}