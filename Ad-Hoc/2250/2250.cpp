#include <iostream>
#include <limits>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

/* Tanto map quanto set mantêm os dados ordenados automaticamente */
typedef map<int, set<string>> rank_t;

void setPlayerRank(rank_t& rank){
    string playerName;
    cin >> playerName;
    int score;
    long long totalScore = 0; // evita possível overflow
    int maxScore = numeric_limits<int>::min();
    int minScore = numeric_limits<int>::max();
    for(size_t i = 0; i < 12; i++){
        cin >> score;
        totalScore += score;
        maxScore = max(maxScore, score);
        minScore = min(minScore, score);
    }
    totalScore -= (maxScore + minScore);
    rank[totalScore].insert(playerName);
}

void displayRankTable(const rank_t& ranking) {
    int pos = 1;
    for (auto it = ranking.rbegin(); it != ranking.rend(); ++it) {
        const int score = it->first;
        const set<string>& players = it->second;
        for (const auto& name : players) {
            cout << pos << " " << score << " " << name << "\n";
        }
        pos += players.size(); // pula conforme quantidade de empatados
    }
}

int main(){
    int numberOfPlayers, testCase = 1;
    while(cin >> numberOfPlayers){
        if(numberOfPlayers == 0) break;
        rank_t rank;
        for(size_t i = 0; i < numberOfPlayers; i++){
            setPlayerRank(rank);
        }
        cout << "Teste " << testCase << "\n";
        displayRankTable(rank);
        cout << "\n";
        testCase++;
    }
    return 0;
}