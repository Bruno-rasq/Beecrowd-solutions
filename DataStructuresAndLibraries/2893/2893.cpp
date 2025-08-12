#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000007;

int Fibonacki(int K, int N) {
    if (N <= K) return N - 1; // Já que os primeiros K termos são 0,1,...,K-1

    vector<int> sequence(K);
    for (int i = 0; i < K; i++) sequence[i] = i;

    long long window_sum = accumulate(sequence.begin(), sequence.end(), 0LL);

    for (int i = K; i < N; i++) {
        sequence.push_back(window_sum % MOD);
        window_sum += sequence.back() - sequence[i - K];
    }

    return sequence[N - 1];
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int K, N;
        cin >> K >> N;
        cout << Fibonacki(K, N) << endl;
    }

    return 0;
}