#include <iostream>
#include <sstream>
#include <cstdint>
#include <algorithm>
using namespace std;

int main() {
    ostringstream oss;
    uint32_t N;
    int K;
    while ((cin >> N >> K) && (N != 0 || K != 0)) {
        uint32_t MIN_ = N;
        uint32_t MAX_ = N;
        for (int i = 0; i < K; i++) {
            int A, B;
            cin >> A >> B;
            // Lê os bits A e B
            int bitA = (N >> A) & 1u;
            int bitB = (N >> B) & 1u;
            // Troca apenas se forem diferentes
            if (bitA != bitB) {
                N ^= (1u << A);
                N ^= (1u << B);
            }
            MAX_ = max(MAX_, N);
            MIN_ = min(MIN_, N);
        }
        oss << N << " " << MAX_ << " " << MIN_ << "\n";
    }
    cout << oss.str();
    return 0;
}