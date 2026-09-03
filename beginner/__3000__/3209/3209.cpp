#include <iostream>

using namespace std;

int main(){

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){

        int j;
        cin >> j;

        int total;
        cin >> total;

        for(int a = 1; a < j: a++){
            int curr;
            cin >> curr;
            total = (total - 1) + curr;
        }

        cout << total << endl;

    }

    return 0;
}