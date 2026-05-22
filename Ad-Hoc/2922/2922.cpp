#include <iostream>
#include <algorithm>
#include <cstdlib>

int main() {
    int n, m;

    while(std::cin >> n >> m) {
        int ans = std::max(std::abs(m - n) - 1, 0);
        std::cout << ans << std::endl;
    }
}