#include <iostream>
#include <vector>
using namespace std;

// DESCOBRIR SE UM QUADRADO N x N É PERFEITO. A SOMATÓRIA DE CADA UMA
// DAS LINHAS E COLUNAS E DIAGONAIS PRINCIPAIS DEVEM RESULTAR NO MESMO
// VALOR. RETORNA -1 SE NÃO FOR PERFEITO, SE FOR PERFEITO RETORNO O
// O VALOR.

#define MATRIX vector<vector<int>>

int main() {

    int n;
    cin >> n;

    MATRIX magic_squad(n, vector<int>(n, 0));

    for(size_t i = 0; i < n; i++)
        for(size_t j = 0; j < n; j++)
            cin >> magic_squad[i][j];

    // CALCULANDO SOMA DAS LINHAS E COLUNAS;
    int magic_sum = 0;

    for(size_t j = 0; j < n; j++)
        magic_sum += magic_squad[0][j];

    for(size_t i = 0; i < n; i++){
        int row = 0;
        int col = 0;
        for(size_t j = 0; j < n; j++){
            row += magic_squad[i][j];
            col += magic_squad[j][i];
        }

        if(row != magic_sum || col != magic_sum){
            cout << -1 << "\n";
            return 0;
        }
    }

    // CALCULANDO SOMA DAS DIAGONAIS PRINCIPAIS
    int diagonal_top_left = 0;
    int diagonal_top_right = 0;
    for(size_t i = 0; i < n; i++){
        diagonal_top_left += magic_squad[i][i];
        diagonal_top_right += magic_squad[i][n - 1 - i];
    }

    if(diagonal_top_left != magic_sum || diagonal_top_right != magic_sum){
        cout << -1 << "\n";
        return 0;
    }

    cout << magic_sum << "\n";
    return 0;
}