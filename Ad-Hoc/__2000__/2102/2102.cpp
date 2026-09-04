#include <iostream>
#include <sstream>
#include <utility>
#include <map>

using Long = long long;
using Coord = std::pair<int, int>;
using Hashmap = std::map<Coord, Long>;

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++) {
        Hashmap dict;
        std::stringstream buff;

        int N, L;
        std::cin >> N >> L;

        for (int j = 0; j < L; j++) {
            int pk, lk, ck, vk;
            std::cin >> pk >> lk >> ck >> vk;

            dict[{lk, ck}] += vk;
        }

        // imprimir ordenado
        for (auto &e : dict) {
            buff << e.first.first  << " "
                 << e.first.second << " "
                 << e.second       << "\n";
        }

        std::cout << buff.str();
        if (i < T - 1) std::cout << "\n";
    }
}