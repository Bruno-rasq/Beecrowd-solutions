#include <iostream>
#include <unordered_map>

int main() {
    int N, S;
    std::cin >> N >> S;

    std::unordered_map<int, long long> freq;

    long long countPair = 0;

    for (int i = 0; i < N; i++) {
        int x;
        std::cin >> x;

        int need = S - x;

        // quantos complementos já apareceram?
        countPair += freq[need];

        // registra o número atual
        freq[x]++;
    }

    std::cout << countPair << '\n';

    return 0;
}