#include <iostream>
#include <cstdint>
#include <algorithm>
#include <vector>
using namespace std;

const int64_t INF = 1e18;

/*
    dp[semana][funcionarios] = menor custo acumulado

    CON -> custo por contratação e treino
    DEM -> custo por demissão de funcionário
    MNS -> custo por semana por funcionário necessário
    CFE -> custo para manter funcionário excedente
    FREQ -> funcionários requisitados por semana
*/
int main() {

    int n;
    int instancia = 0;
    while ((cin >> n) && (n != 0)) {

        int64_t dp[201][51];
        for (int i = 0; i <= 200; i++)
            for (int j = 0; j <= 50; j++)
                dp[i][j] = INF;

        dp[0][0] = 0;

        vector<int> FREQ(n);
        for (int i = 0; i < n; i++)
            cin >> FREQ[i];

        int CON, DEM, MNS, CFE;
        cin >> CON >> DEM >> MNS >> CFE;

        for (int week = 1; week <= n; week++)
            for (int prev = 0; prev <= 50; prev++) {
                if (dp[week - 1][prev] == INF) continue;
                for (int curr = FREQ[week - 1]; curr <= 50; curr++) {
                    int64_t cost = 0;
                    // contratação
                    if (curr > prev) cost += (curr - prev) * CON;
                    // demissão
                    else cost += (prev - curr) * DEM;
                    // funcionários necessários
                    cost += FREQ[week - 1] * MNS;
                    // funcionários excedentes
                    cost += (curr - FREQ[week - 1]) * CFE;

                    dp[week][curr] = min(dp[week][curr], dp[week - 1][prev] + cost);
                }
            }

        int64_t ans = INF;
        for (int employees = 0; employees <= 50; employees++) {
            if (dp[n][employees] == INF) continue;

            ans = min( ans, dp[n][employees] + (int64_t)employees * DEM);
        }

        cout << "Instancia " << ++instancia << "\n" << ans << "\n\n";
    }
    return 0;
}