#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;

int main() {

    vector<uint64_t> fib = {0, 1};
    while(fib.size() < 61){
        uint64_t last = fib[fib.size() - 1];
        uint64_t secondlast = fib[fib.size() - 2];
        fib.push_back(last + secondlast);
    }
    
    int T;
    cin >> T;

    for(size_t idx = 0; idx < T; idx++){
        int N;
        cin >> N;
        cout << "Fib(" << N << ") = " << fib[N] << "\n";
    }
    
    return 0;
}