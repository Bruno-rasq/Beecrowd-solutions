#include <iostream>
#include <unordered_map>
using namespace std;

const unordered_map<char, int> leds = {
    {'0', 6}, {'1', 2}, {'2', 5}, {'3', 5}, {'4', 4},
    {'5', 5}, {'6', 6}, {'7', 3}, {'8', 7}, {'9', 6},
};


int main() {
    int n;
    cin >> n;

    for(size_t i = 0; i < n; i++){
        string number;
        cin >> number;

        int ans = 0;
        for(char& chr : number)
            ans += leds.at(chr);

        cout << ans << " leds\n";
    }

    return 0;
}