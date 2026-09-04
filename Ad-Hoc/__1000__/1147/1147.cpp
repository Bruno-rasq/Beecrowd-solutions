#include <bits/stdc++.h>
using namespace std;

const int PAWNDELTA[2][2] = { {-1, -1}, {-1, 1} };
const int HORSEDELTA[8][2] = {
    {-2, -1}, {-2,  1}, {-1, -2}, {-1,  2},
    { 1, -2}, { 1,  2}, { 2, -1}, { 2,  1}};

int main() {
    int T = 1;
    string pos;
    while ((cin >> pos) && (pos != "0")) {
        int horse_x = pos[0] - '1';
        int horse_y = pos[1] - 'a';

        set<pair<int, int>> dangerousPos;
        for (size_t i = 0; i < 8; i++) {
            cin >> pos;
            int pawn_x = pos[0] - '1';
            int pawn_y = pos[1] - 'a';
            for (auto &delta : PAWNDELTA) {
                int px = pawn_x + delta[0];
                int py = pawn_y + delta[1];
                if (px < 0 || px > 7 || py < 0 || py > 7) continue;
                dangerousPos.insert({px, py});
            }
        }

        int ans = 0;
        for (auto &delta : HORSEDELTA) {
            int hx = horse_x + delta[0];
            int hy = horse_y + delta[1];
            if (hx < 0 || hx > 7 || hy < 0 || hy > 7) continue;
            if (dangerousPos.count({hx, hy})) continue;
            ans++;
        }

        cout << "Caso de Teste #" << T++ << ": " << ans << " movimento(s).\n";
    }
}