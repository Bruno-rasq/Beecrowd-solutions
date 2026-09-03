#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <tuple>
#include <iomanip>
#include <algorithm>

#define SUCESS "Missao completada com sucesso"
#define FAIL "You Are Dead"

typedef std::vector<std::tuple<double, int>> ITENS;

// tabela de armas e dano por municao
const std::map<std::string, double> WEAPONS = {
    {"HANDGUN",     2.0},    {"RED9",       3.5},
    {"BLACKTAIL",   3.5},    {"MATILDA",    2.0},
    {"HANDCANNON",  60.0},   {"STRIKER",    12.0},
    {"TMP",         1.2},    {"RIFLE",      12.0}
};

// tabela de inimigos e a quantidade de vida de cada
const std::map<std::string, double> ENEMIES = {
    {"GANADOS",     50},    {"COBRAS",          40},
    {"ZEALOT",      75},    {"COLMILLOS",       60},
    {"GARRADOR",    125},   {"LASPLAGAS",       100},
    {"GATLINGMAN",  150},   {"REGENERATOR",     250},
    {"ELGIGANTE",   500},   {"DR.SALVADOR",     350}
};

std::vector<std::vector<int>> KnapsackProblem(ITENS& itens, int capacity) {
    
    int rows = itens.size() + 1;
    int cols = capacity + 1;
    std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, 0));

    for (int i = 1; i < rows; i++) {
        
        double curr_damage = std::get<0>(itens[i - 1]);
        int curr_ammo = std::get<1>(itens[i - 1]);

        for (int j = 0; j < cols; j++) {
            if (j < curr_ammo) dp[i][j] = dp[i - 1][j];
            else {
                int remaining = j - curr_ammo;
                int added_value = dp[i - 1][remaining] + (int)curr_damage;
                dp[i][j] = std::max(dp[i - 1][j], added_value);
            }
        }
    }
    return dp;
}

int main() {
    using namespace std;
    int n_weapons, n_enemies, amount_ammunation, amount_enemies, capacity;
    string weapon_name, enemy_name;

    while (cin >> n_weapons) {
        ITENS weapons;
        for (int i = 0; i < n_weapons; i++) {
            cin >> weapon_name >> amount_ammunation;
            double damage = WEAPONS.at(weapon_name) * (double) amount_ammunation;
            weapons.push_back({damage, amount_ammunation});
        }

        int total_enemies_HP = 0;
        cin >> n_enemies;
        for (int i = 0; i < n_enemies; i++) {
            cin >> enemy_name >> amount_enemies;
            total_enemies_HP += ENEMIES.at(enemy_name) * amount_enemies;
        }

        cin >> capacity;
        auto dp = KnapsackProblem(weapons, capacity);
        double max_damage = dp[n_weapons][capacity];

        cout << (total_enemies_HP - max_damage <= 0 ? SUCESS : FAIL) << endl << endl;
    }

    return 0;
}