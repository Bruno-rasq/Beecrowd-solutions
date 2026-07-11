
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {

    int N;
    bool first = true;
    while((cin >> N) && (N != 0)){

        if(!first) cout << "\n";
        first = false;
        
        map<string, map<string, vector<string>>> bucket;
        cin.ignore();
        for (int i = 0; i < N; i++) {
            string name, color, size;
            getline(cin, name);
            cin >> color >> size;
            cin.ignore();
            bucket[color][size].push_back(name);
        }
        for (auto &[color, sizes] : bucket) {
            for (auto it = sizes.rbegin(); it != sizes.rend(); ++it) {
                auto names = it->second;
                sort(names.begin(), names.end());
    
                for (const auto &name : names)
                    cout << color << ' ' << it->first << ' ' << name << '\n';
            }
        }
    }
}