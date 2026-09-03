#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
    unordered_map<int, int> dp = {{1, 1}, {2, 5}};
    for(size_t i = 3; i <= 100; i++){
        int value = (i * i) + dp.at(i - 1);
        dp[i] = value;
    }
    int n;
    while(cin >> n){
        if(n == 0) break;
        cout << dp[n] << "\n";
    }
}