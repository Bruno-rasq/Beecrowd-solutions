#include <iostream>
#include <map>
#include <cctype>
using namespace std;

int main() {
    string line;
    getline(cin, line);

    map<string, int> freq;

    // Conta frequência dos dígrafos
    for(size_t pos = 0; pos + 1 < line.size(); pos++) {
        string digrafo = line.substr(pos, 2);
        for(char& c : digrafo)
            c = tolower((unsigned char)c);
        freq[digrafo]++;
    }

    // Agrupa por frequência absoluta
    map<int, map<string, int>> freqAbsolute;
    for(const auto& [digrafo, frequence] : freq) {
        freqAbsolute[frequence][digrafo] = 0;
    }

    // Pega maior frequência
    for(auto it = freqAbsolute.rbegin(); it != freqAbsolute.rend(); ++it) {
        int freqAbs = it->first;
        // map já mantém ordem lexicográfica
        for(const auto& [digrafo, value] : it->second) {
            cout << digrafo << ":" << freqAbs << "\n";
            return 0;
        }
    }
}