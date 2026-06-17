#include <iostream>
#include <numeric>
using namespace std;

// x = [N/A] + [N/B] - [N/MMC(A,B)]

int mmc(int a, int b){
    if(a == 0 || b == 0) return 0;
    return (a * b) / gcd(a, b);
}

int main(){
    int N, A, B;
    while((cin >> N >> A >> B) && (A != 0 && B != 0 && N != 0)){
        int ans = (N / A) + (N / B) - (N / mmc(A,B));
        cout << ans << "\n";
    }
}