#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

const unordered_map<string, int> INDEXS = {
    {"0", 0},{"1", 1},{"00", 0},{"01", 1},{"11", 2},{"10", 3}};

string identify_table(const unordered_set<string>& bits) {
    if (bits.size() > 1) return "Contingencia";
    if (bits.count("1")) return "Tautologia";
    return "Contradicao";
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        int amount_vars;
        cin >> amount_vars;
        unordered_set<string> bits;
        stringstream buffer;
        cout << "Mapa de Karnaugh\n";
        if (amount_vars == 2) {
            vector<vector<string>> kt(2, vector<string>(2));
            for (int i = 0; i < 4; i++) {
                string a, b, dash, s;
                cin >> a >> b >> dash >> s;
                int row = INDEXS.at(b);
                int col = INDEXS.at(a);
                kt[row][col] = s;
                bits.insert(s);
            }
            buffer << "  0 1\n";
            buffer << "0|" << kt[0][0] << " " << kt[0][1] << "\n";
            buffer << "1|" << kt[1][0] << " " << kt[1][1] << "\n";
            cout << buffer.str();
        }
        else if (amount_vars == 3) {
            vector<vector<string>> kt(2, vector<string>(4));
            for (int i = 0; i < 8; i++) {
                string a, b, c, dash, s;
                cin >> a >> b >> c >> dash >> s;
                int row = INDEXS.at(c);
                int col = INDEXS.at(a+b);
                kt[row][col] = s;
                bits.insert(s);
            }
            buffer << "  00 01 11 10\n";
            buffer << "0|" << kt[0][0] << "  " << kt[0][1] << "  " << kt[0][2] << "  " << kt[0][3] << "\n";
            buffer << "1|" << kt[1][0] << "  " << kt[1][1] << "  " << kt[1][2] << "  " << kt[1][3] << "\n";
            cout << buffer.str();
        }
        else {
            vector<vector<string>> kt(4, vector<string>(4));
            for (int i = 0; i < 16; i++) {
                string a, b, c, d, dash, s;
                cin >> a >> b >> c >> d >> dash >> s;
                int row = INDEXS.at(c + d);
                int col = INDEXS.at(a + b);
                kt[row][col] = s;
                bits.insert(s);
            }
            buffer << "   00 01 11 10\n";
            buffer << "00|" << kt[0][0] << "  " << kt[0][1] << "  " << kt[0][2] << "  " << kt[0][3] << "\n";
            buffer << "01|" << kt[1][0] << "  " << kt[1][1] << "  " << kt[1][2] << "  " << kt[1][3] << "\n";
            buffer << "11|" << kt[2][0] << "  " << kt[2][1] << "  " << kt[2][2] << "  " << kt[2][3] << "\n";
            buffer << "10|" << kt[3][0] << "  " << kt[3][1] << "  " << kt[3][2] << "  " << kt[3][3] << "\n";
            cout << buffer.str();
        }
        cout << identify_table(bits) << "\n";
        if (n) cout << "\n";
    }
}