#include <iostream>
#include <string>
#include <cstdio> // para scanf

using namespace std;

string crypt[10][2] = {
    {"GQaku", "0"},
    {"ISblv", "1"},
    {"EOYcmw", "2"},
    {"FPZdnx", "3"},
    {"JTeoy", "4"},
    {"DNXfpz", "5"},
    {"AKUgq", "6"},
    {"CMWhr", "7"},
    {"BLVis", "8"},
    {"HRjt", "9"}
};

int main() {
    int n;
    scanf("%d", &n);
    string dummy;
    getline(cin, dummy); // consome o '\n' que sobra do scanf

    for (int i = 0; i < n; i++) {
        string frase;
        getline(cin, frase);
        string incrypt = "";

        for (char ch : frase) {
            if (ch == ' ') continue;

            for (int j = 0; j < 10; j++) {
                if (crypt[j][0].find(ch) != string::npos) {
                    incrypt += crypt[j][1];
                    break;
                }
            }

            if (incrypt.length() >= 12) break;
        }

        cout << incrypt.substr(0, 12) << endl;
    }

    return 0;
}