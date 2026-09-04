#include <iostream>
#include <cctype>
#include <string>  // Necessário para usar string

using namespace std;

int main() {
    int n, soma = 0;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string line, digits;
        cin >> line;

        for (const char& c : line) {
            if (isdigit(c)) {
                digits += c;
            }
        }

        soma += stoi(digits);
    }

    cout << soma << endl;
    return 0;
}
