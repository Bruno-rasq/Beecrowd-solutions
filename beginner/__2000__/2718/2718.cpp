#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    ostringstream buffer;
    while (n--) {
        uint64_t leds;
        cin >> leds;
        uint64_t maxseq = 0;
        uint64_t currseq = 0;
        for (int i = 0; i < 64; i++) {
            if (leds & (1ULL << i)) {
                currseq++;
                maxseq = max(maxseq, currseq);
            } else {
                currseq = 0;
            }
        }
        buffer << maxseq << '\n';
    }
    cout << buffer.str();
    return 0;
}