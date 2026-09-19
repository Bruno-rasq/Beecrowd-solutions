#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <iomanip>
using namespace std;

// CALCULAR A DOSE CERTA DO ANTÍDOTO PARA MATAR A BACTÉRIA.
// A BACTÉRIA ESTÁ EM UMA GRADE N x N, ONDE OS VALOR 1 REPRESENTAM
// A BACTERIA (ÚNICA) E OS ZEROS A PARTE SEM BACTÉRIA.

struct Cell {
    bool isInfected;
    bool visited;
};

// IDEIA: É NECESSÁRIO CALCULAR A AREA INTERNA E PERÍMETRO DA BACTÉRIA
// ISSO É, AREA TOTAL DO GRID MENOS A AREA EXTERNA A BACTERIA. PRECISO
// DE UM LOOP QUE ITERE SOBRE AS CELULAS NAS BORDAS DO GRID E EXECUTE
// UMA BFS/DFS VARRENDO A AREA EXTERNA.

#define BOARD vector<vector<Cell>>
#define COORD pair<int, int>

const vector<COORD> DELTA = {
    {-1, 0},
    {0, 1},
    {1, 0},
    {0, -1}
};

void BFS(BOARD& board, int& area, int x, int y){
    // SE A CELULA FOR INFECTADA OU JÁ TIVER SIDO VISITADA,
    // ELA NÃO FAZ PARTE DA AREA EXTERNA.
    if(board[x][y].isInfected || board[x][y].visited)
        return;

    queue<COORD> Q;

    Q.push({x, y});
    board[x][y].visited = true;
    area++;

    while(!Q.empty()){
        COORD current_cell = Q.front();
        Q.pop();

        for(const COORD delta : DELTA){
            int nx = current_cell.first + delta.first;
            int ny = current_cell.second + delta.second;

            if(nx >= 0 && nx < board.size() &&
               ny >= 0 && ny < board[0].size())

                if(!board[nx][ny].visited &&
                   !board[nx][ny].isInfected){

                    board[nx][ny].visited = true;
                    area++;
                    Q.push({nx, ny});
                }
        }
    }
}

int main(){
    int n;
    cin >> n;

    while(n--){
        int X;
        cin >> X;

        BOARD board(X, vector<Cell>(X, {false, false}));

        for(int i = 0; i < X; i++)
            for(int j = 0; j < X; j++)
                cin >> board[i][j].isInfected;

        int total_area = X * X;
        int extern_area = 0;

        // CIMA
        for(int j = 0; j < X; j++)
            BFS(board, extern_area, 0, j);

        // DIREITA
        for(int i = 1; i < X - 1; i++)
            BFS(board, extern_area, i, X - 1);

        // BAIXO
        for(int j = X - 1; j >= 0; j--)
            BFS(board, extern_area, X - 1, j);

        // ESQUERDA
        for(int i = X - 2; i > 0; i--)
            BFS(board, extern_area, i, 0);

        // A AREA DA BACTERIA E DADA PELA SOMA DA BORDA (1)
        // COM O CONTEUDO INTERNO (0 INTERNO), DIVIDIDA POR 2.
        //
        // AREA TOTAL - AREA EXTERNA = BORDA + CONTEUDO INTERNO.

        float bacteria_area = (total_area - extern_area) / 2.0;

        cout << fixed << setprecision(2) << bacteria_area << "\n";
    }

    return 0;
}