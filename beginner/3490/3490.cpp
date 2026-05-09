#include <iostream>
#include <string>

int main() {
    char a, b, c, d;

    while (std::cin >> a >> b >> c >> d) {
        std::string ans;

        ans += a;
        ans += b;
        ans += c;
        ans += d;
        ans += '\n';

        std::cout << ans;
    }

    return 0;
}