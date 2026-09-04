#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

/*
    Quantidade de dados <= 13
    Quantidade de faces <= 20
    Soma máxima = 13 * 20 = 260
*/

int main() {

    int testes;
    cin >> testes;
    while (testes--) {
        int somaAlvo, quantidadeDados, faces;
        cin >> somaAlvo >> quantidadeDados >> faces; 
        
        long long total = 1;
        // dp[dadosUsados][somaAtual]
        long long dp[14][261] = {0};
        // estado base
        dp[0][0] = 1;
        for (int i = 1; i <= quantidadeDados; i++) {
            total *= faces;
            for (int j = 1; j <= somaAlvo; j++)
                for (int k = 1; k <= faces; k++)
                    if (j - k >= 0)
                        dp[i][j] += dp[i - 1][j - k];
        }

        long long combinacoesFavoraveis = dp[quantidadeDados][somaAlvo];
        long double probabilidade = (long double) combinacoesFavoraveis / total;
        stringstream ss;

        ss << fixed
           << setprecision(faces)
           << probabilidade;

        cout << ss.str() << "\n";
    }
}