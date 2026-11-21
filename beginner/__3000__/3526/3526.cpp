#include <iostream>
using namespace std;

int main() {

    string ans = "SIM";

    int S, P, N;
    cin >> S >> P >> N;

    if(P > (S - (P * N)))
        ans = "NAO";

    cout << ans << "\n";
    
    return 0;
}