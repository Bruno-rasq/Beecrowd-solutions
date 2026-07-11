#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x, y;
    cin >> n;
    while(n--){
        cin >> x >> y;
        if(x == 0 && y == 0){
        	cout << "0\n";
        	continue;
        }
        int ans = pow(26, x) * pow(10, y);
        ans %= 2147483648;
        cout << ans << "\n";
    }
}