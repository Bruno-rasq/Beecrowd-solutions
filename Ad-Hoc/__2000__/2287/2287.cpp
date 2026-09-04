#include <iostream>
#include <map>
#include <array>
#include <vector>
#include <algorithm>
using namespace std;

const int passwordsize = 6;

void configAssociationKeys(vector<vector<int>>& PWD) {
    map<char, array<int, 2>> Keys;
    int ax, ay, bx, by, cx, cy, dx, dy, ex, ey;
    cin >> ax >> ay;
    Keys['A'] = {ax, ay};
    cin >> bx >> by;
    Keys['B'] = {bx, by};
    cin >> cx >> cy;
    Keys['C'] = {cx, cy};
    cin >> dx >> dy;
    Keys['D'] = {dx, dy};
    cin >> ex >> ey;
    Keys['E'] = {ex, ey};
    for(size_t i = 0; i < passwordsize; i++){
        char key;
        cin >> key;
        PWD[i].push_back(Keys[key][0]);
        PWD[i].push_back(Keys[key][1]);
    }
}

int amostFrequentDigit(vector<int>& digits){
    vector<int> freq(10, 0);
    int maxFreq = 0;
    for(int d : digits){
        freq[d]++;
        maxFreq = max(maxFreq, freq[d]);
    }
    for(int i = 0; i < 10; i++)
        if(freq[i] == maxFreq)
            return i;

    return 0;
}

int main() {
    int NOA;
    int testCase = 1;
    while(cin >> NOA){
        if(NOA == 0) break;
        vector<vector<int>> PWD(passwordsize);
        for(int i = 0; i < NOA; i++)
            configAssociationKeys(PWD);

        string correctPassword = "";
        for(int i = 0; i < passwordsize; i++){
            int digit = amostFrequentDigit(PWD[i]);
            correctPassword += to_string(digit) + " ";
        }
        cout << "Teste " << testCase++ << "\n";
        cout << correctPassword << "\n" << "\n";
    }
    return 0;
}