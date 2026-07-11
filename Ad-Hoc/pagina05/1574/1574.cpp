#include <bits/stdc++.h>
using namespace std;

int main() {
    int t, n;
    cin >> t;
    while(t--){
        cin >> n;
        cin.ignore();

        int x = 0; 
        unordered_map<int, string> INSTRUCTIONS; 

        for(int inst = 1; inst <= n; inst++){
            string instruction;
            getline(cin, instruction);

            if(instruction.starts_with("SAME AS")){
                int nth = stoi(instruction.substr(8));
                instruction = INSTRUCTIONS.at(nth);
            }

            if(instruction == "LEFT") x--;
            if(instruction == "RIGHT") x++;

            INSTRUCTIONS[inst] = instruction;
        }
        cout << x << "\n";
    }
}
