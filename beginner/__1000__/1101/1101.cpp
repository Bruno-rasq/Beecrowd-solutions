#include <bits/stdc++.h>
using namespace std;

int main(){
    while (true) {
        int n, m;
        cin >> n >> m;
        if (n <= 0 || m <= 0) break;
        int i = min(n, m);
        int f = max(n, m);
        int sum = 0;
        string ans = "";
        for(size_t num=i; num<=f; num++){
            ans += to_string(num) + " ";
            sum += num;
        }
        ans += "Sum=" + to_string(sum) + "\n";
        cout << ans;
    }
    return 0;
}