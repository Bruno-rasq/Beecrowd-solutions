#include <iostream>
#include <cstdint>
#include <vector>
using namespace std;

int main() {

    vector<int64_t> fib;
    fib.push_back(0);
    fib.push_back(1);

    while(fib.size() <= 60){
        int64_t a = fib[fib.size() - 1];
        int64_t b = fib[fib.size() - 2];
        fib.push_back(a + b);
    }

    int n;
    cin >> n;
    for(size_t i = 0; i < n; i++){
        int idx;
        cin >> idx;
        cout << "Fib(" << idx << ") = " << fib[idx] << "\n";
    }
    return 0;
}