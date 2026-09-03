#include <iostream>
#include <string>

int digitSum(int x) {
    int sum = 0;
    while (x > 0) {
        sum += x % 10;
        x /= 10;
    }
    return sum;
}

int main() {
    int n;
    while (std::cin >> n && n != 0) {
        while (n--) {
            std::string s;
            std::cin >> s;
            int odd = 0;
            int even = 0;
            bool turn = false;
            for (int i = s.size() - 1; i >= 0; i--) {
                int d = s[i] - '0';
                if (!turn)
                    odd += d;
                else
                    even += d;
                turn = !turn;
            }
            int ans =
                digitSum(odd) +
                digitSum(even);
            std::cout << ans << '\n';
        }
    }
}