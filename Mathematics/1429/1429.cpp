#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

unordered_map<int, int> fatorial = {
    {1, 1}, {2, 2}, {3, 6}, {4, 24}, {5, 120}};

int main() {
    int n;
    while ((cin >> n) && (n != 0)) {
        vector<int> digits;
        while (n > 0) {
            digits.push_back(n % 10);
            n /= 10;
        }
        int ans = 0;
        for (size_t i = 0; i < digits.size(); i++)
            ans += digits[i] * fatorial[i + 1];
        cout << ans << "\n";
    }
}