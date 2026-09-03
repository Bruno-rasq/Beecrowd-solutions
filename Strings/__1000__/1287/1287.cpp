#include <iostream>
#include <string>

using namespace std;

int main() {
    const string LIMITE = "2147483647";

    string line;
    while (getline(cin, line)) {
        string num = "";
        bool is_valid = true;

        for (char chr : line) {
            if (chr >= '0' && chr <= '9') {
                num += chr;
            } else if (chr == 'o' || chr == 'O') {
                num += '0';
            } else if (chr == 'l') {
                num += '1';
            } else if (chr == ' ' || chr == ',') {
                continue;
            } else {
                is_valid = false;
                break;
            }
        }

        // Remove zeros à esquerda
        size_t first_non_zero = num.find_first_not_of('0');
        if (first_non_zero != string::npos) {
            num = num.substr(first_non_zero);
        } else if (!num.empty()) {
            num = "0";
        }

        bool error = num.empty() ||
                     num.length() > LIMITE.length() ||
                     (num.length() == LIMITE.length() && num > LIMITE);

        cout << (is_valid && !error ? num : "error") << endl;
    }

    return 0;
}
