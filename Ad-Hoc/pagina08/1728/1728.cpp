#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int REV(string s) {
    reverse(s.begin(), s.end());
    return stoi(s);
}

int main() {
    while (true) {
        string expr;
        cin >> expr;
        size_t p = expr.find('+');
        size_t q = expr.find('=');
        string A = expr.substr(0, p);
        string B = expr.substr(p + 1, q - p - 1);
        string C = expr.substr(q + 1);

        if (A == "0" && B == "0" && C == "0") break;
        bool ans = REV(A) + REV(B) == REV(C);

        cout << (ans ? "True" : "False") << '\n';
    } 
    cout << "True\n";

    return 0;
}