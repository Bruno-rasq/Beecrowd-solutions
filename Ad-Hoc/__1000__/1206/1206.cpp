#include <iostream>
#include <vector>
#include <array>
using namespace std;

struct Coord { int row, col; };
struct XadrezPiece { Coord pos; char type; };

struct BoardState {
    array<bool, 64> positions{};
    void set(int row, int col) { positions[row * 8 + col] = true; }
    bool get(int row, int col) { return positions[row * 8 + col]; }
};

/* movimentos */
const vector<Coord> pawnmove = {{-1,-1}, {-1,1}};
const vector<Coord> ver_hor = {{1,0}, {-1,0}, {0,1}, {0,-1}};
const vector<Coord> diagonal = {{-1,-1}, {-1,1}, {1,-1}, {1,1}};
const vector<Coord> kingmove = {
    {1,0}, {-1,0}, {0,1}, {0,-1},
    {-1,-1}, {-1,1}, {1,-1}, {1,1}
};

/* movimentos de 1 casa */
void A(BoardState& attack, BoardState& initialState,
       XadrezPiece& piece, const vector<Coord>& delta){

    for(auto [dx, dy]: delta){
        int nx = piece.pos.row + dx;
        int ny = piece.pos.col + dy;

        if(nx >= 0 && nx < 8 && ny >= 0 && ny < 8){
            // CORREÇÃO: sempre marca ataque
            attack.set(nx, ny);
        }
    }
}

/* movimentos infinitos */
void B(BoardState& attack, BoardState& initialState,
       XadrezPiece& piece, const vector<Coord>& delta){

    for (auto [dr, dc] : delta) {
        int r = piece.pos.row + dr;
        int c = piece.pos.col + dc;

        while (r >= 0 && r < 8 && c >= 0 && c < 8) {

            // CORREÇÃO: marca ANTES de checar bloqueio
            attack.set(r, c);

            if(initialState.get(r, c)) break;

            r += dr;
            c += dc;
        }
    }
}

/* gera mapa de ataque */
void buildAttack(BoardState& attack, BoardState& initialState,
                 vector<XadrezPiece>& pieces){

    attack.positions.fill(false);

    for(auto &piece : pieces){
        switch(piece.type){
            case 'P': A(attack, initialState, piece, pawnmove); break;
            case 'T': B(attack, initialState, piece, ver_hor);  break;
            case 'B': B(attack, initialState, piece, diagonal); break;
            case 'R': B(attack, initialState, piece, ver_hor),
                      B(attack, initialState, piece, diagonal); break;
            case 'W': A(attack, initialState, piece, kingmove); break;
        }
    }
}

int main() {

    int n;
    while(cin >> n){

        BoardState attackPositions, initialState;
        vector<XadrezPiece> pieces;

        for(int i = 0; i < n; i++){
            string s;
            cin >> s;

            char piece = s[0];
            int col = s[1] - 'a';
            int row = s[2] - '1';

            initialState.set(row, col);
            pieces.push_back({{row, col}, piece});
        }

        string WK;
        cin >> WK;

        int kc = WK[1] - 'a';
        int kr = WK[2] - '1';

        // posição do rei também ocupa o tabuleiro
        initialState.set(kr, kc);

        // mapa inicial
        buildAttack(attackPositions, initialState, pieces);

        bool inCheck = attackPositions.get(kr, kc);

        bool hasEscape = false;

        // testar movimentos do rei
        for(auto [dx, dy]: kingmove){
            int nr = kr + dx;
            int nc = kc + dy;

            if(nr < 0 || nr >= 8 || nc < 0 || nc >= 8) continue;

            // salva estado original
            bool hadPiece = initialState.get(nr, nc);

            // simula movimento
            initialState.positions[kr * 8 + kc] = false;
            initialState.positions[nr * 8 + nc] = true;

            // remove peça capturada (se houver)
            vector<XadrezPiece> newPieces;
            for(auto &p : pieces){
                if(!(p.pos.row == nr && p.pos.col == nc))
                    newPieces.push_back(p);
            }

            BoardState newAttack;
            buildAttack(newAttack, initialState, newPieces);

            if(!newAttack.get(nr, nc)){
                hasEscape = true;
            }

            // desfaz
            initialState.positions[nr * 8 + nc] = hadPiece;
            initialState.positions[kr * 8 + kc] = true;

            if(hasEscape) break;
        }

        cout << ((inCheck && !hasEscape) ? "SIM\n" : "NAO\n");
    }

    return 0;
}