#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    while (t != 0){
        for(int i = 0; i < t; i++){
            int n;
            cin >> n;
            cout << ((n - 1) % 2 == 0 ? 2 * n - 1: 2 * n - 2 )<< endl;
        }
        cin >> t;
    }
    return 0;
}