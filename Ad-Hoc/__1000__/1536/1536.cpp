#include <bits/stdc++.h>
using namespace std;

struct Team {
    int points = 0;      // Pontos acumulados
    int goals = 0;       // Gols marcados
    int awayGoals = 0;   // Gols marcados fora de casa
};

void Play(Team &home, Team &away) {
    int x, y;
    scanf("%d x %d", &x, &y);

    home.goals += x;
    away.goals += y;

    // Gols do visitante
    away.awayGoals += y;

    if (x == y) {
        home.points++;
        away.points++;
    } else if (x > y) {
        home.points += 3;
    } else {
        away.points += 3;
    }
}

int main() {
    int n;
    cin >> n;

    while (n--) {
        Team team1, team2;

        // Jogo 1: Time 1 em casa
        Play(team1, team2);

        // Jogo 2: Time 2 em casa
        Play(team2, team1);

        if (team1.points > team2.points) {
            cout << "Time 1\n";
        } else if (team2.points > team1.points) {
            cout << "Time 2\n";
        } else {
            int goalDiff = team1.goals - team2.goals;

            if (goalDiff > 0) {
                cout << "Time 1\n";
            } else if (goalDiff < 0) {
                cout << "Time 2\n";
            } else if (team1.awayGoals > team2.awayGoals) {
                cout << "Time 1\n";
            } else if (team2.awayGoals > team1.awayGoals) {
                cout << "Time 2\n";
            } else {
                cout << "Penaltis\n";
            }
        }
    }

    return 0;
}