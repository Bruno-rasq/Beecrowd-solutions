#include <iostream>
#include <set>
using namespace std;

int main(){

    set<int> stickers;
    int n, curr, repeated_stickers = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        cin >> curr;
        int len = stickers.size();
        stickers.insert(curr);

        repeated_stickers += len == stickers.size() ? 1 : 0;
    }

    cout << stickers.size() << endl;
    cout << repeated_stickers << endl;

    return 0;
}