#include <iostream>
using namespace std;

int main() {
    int T = 1;
    while(true){
        int R, W, H;
        cin >> R;
        if(R == 0) break;
        cin >> W >> H;
        bool ans = false;
        if(W * W + H * H <= 4 * R * R) ans = true;
        cout << "Pizza " << T << (
            ans ? " fits on the table.\n" : " does not fit on the table.\n");
        T++;
    }
    return 0;
}