
#include <iostream>
#include <map>
#include <string>
#include <algorithm> // std::transform
#include <cctype>    // std::tolower

using namespace std;

string toLower(const string& s) {
    string result = s;
    transform(result.begin(), result.end(), result.begin(),
              [](unsigned char c) { return tolower(c); });
    return result;
}

int main () {
    string nome;
    map<string, string> criancas;

    while (getline(cin, nome)) {
        criancas[toLower(nome)] = nome;
    }

    auto ultima = prev(criancas.end());
    cout << ultima->second << endl;

    return 0;
}