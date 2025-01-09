#include <iostream>

using namespace std;

int main() {

    int n, wins = 0;
    cin >> n;

    for(int i = 0; i < n; i++){
        string curr;
        cin >> curr;

        size_t pos = curr.find("CD");
        if(pos == string::npos){
            wins++;
        }
    }

    cout << wins << endl;
    return 0;

}