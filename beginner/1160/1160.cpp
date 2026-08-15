#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        int population_A, population_B;
        float growing_rate_A, growing_rate_B;
        cin >> population_A >> population_B >> growing_rate_A >> growing_rate_B;

        int time = 0;
        while (time <= 100 && population_A <= population_B) {
            population_A += (int)(population_A * growing_rate_A / 100);
            population_B += (int)(population_B * growing_rate_B / 100);
            time++;
        }

        if (time > 100) cout << "Mais de 1 seculo.\n";
        else cout << time << " anos.\n";
    }
    return 0;
}