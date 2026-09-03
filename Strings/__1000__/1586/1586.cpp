#include <iostream>
#include <vector>
using namespace std;

struct DATA {
    string name;
    long long force_base;
};

string binary_search(vector<DATA>& names){
    int LEFT = 0;
    int RIGHT = names.size() - 1;

    while (LEFT <= RIGHT){
        int MID = (LEFT + RIGHT) / 2;
        long long forceA = 0, forceB = 0;

        // Team A: todos os estudantes antes e o estudante sorteado.
        for(int i = 0; i <= MID; i++)
            forceA += names[i].force_base * (MID - i + 1);

        // Team B: todos os estudantes depois do estudante sorteado.
        for(int i = MID + 1; i < names.size(); i++)
            forceB += names[i].force_base * (i - MID);

        if(forceA == forceB)
            return names[MID].name;

        if(forceA > forceB)
            RIGHT = MID - 1;
        else
            LEFT = MID + 1;
    }

    return "Impossibilidade de empate.";
}

int main() {
    int n;

    while((cin >> n) && n != 0){

        vector<DATA> names;

        for(size_t i = 0; i < n; i++){
            long long force = 0;
            string name;

            cin >> name;

            for(char chr : name)
                force += (int)chr;

            names.push_back({name, force});
        }

        cout << binary_search(names) << "\n";
    }

    return 0;
}