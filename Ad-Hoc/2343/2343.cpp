#include <bits/stdc++.h>
using namespace std;

int quadrantes[501][501];

int main(){
    
    memset(quadrantes, false, sizeof(quadrantes));
    
    int n, x, y;
    cin >> n;
    
    for(size_t i = 0; i < n; i++){
        cin >> x >> y;
        if(quadrantes[x][y] == true){
            cout << "1\n";
            return 0;
        }
        quadrantes[x][y] = true;
    }
    
    cout << "0\n";
    return 0;
}