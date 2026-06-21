#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;
    while (T--) {
        
        string unlockingWord, secretWord;
        int cryptexsize;

        cin >> cryptexsize >> unlockingWord >> secretWord;
    
        char key;
        int idx = 0;
        for(size_t i = 0; i < secretWord.size(); i++){
            char curr = secretWord[i];
            if(curr != '_') {
                idx = i;
                key = curr;
                break;
            }
        }

        string cryptex[cryptexsize];
        int Uidx = -1;
        for(size_t i = 0; i < cryptexsize; i++){
            cin >> cryptex[i];
            if (i == idx){
                for(size_t j = 0; j < 26; j++){
                    if(cryptex[i][j] == unlockingWord[idx]){
                        Uidx = j;
                        break;
                    }
                }
            }
        }

        int Kidx = -1;
        for(size_t col = 0; col < 26; col++)
            if(cryptex[idx][col] == key){
                Kidx = col;
                break;
            }
    
        string ans = "";
        int dist = (Kidx - Uidx + 26) % 26;
        for(size_t row = 0; row < cryptexsize; row++){
            if(row == idx){
                ans += key;
                continue;
            }
            for(size_t col = 0; col < 26; col++){
                if(cryptex[row][col] == unlockingWord[row]){
                    ans += cryptex[row][(col + dist) % 26];
                    break;
                }
            }
        }

        cout << unlockingWord << " " << ans << "\r\n";
    }
}