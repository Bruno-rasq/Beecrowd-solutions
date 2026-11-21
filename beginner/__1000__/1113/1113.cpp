#include <iostream>
#include <cstdint>
using namespace std;

int main() {

    uint32_t x, y;

    while(cin >> x >> y && x != y){
        cout << (x < y ? "Crescente" : "Decrescente") << "\n";
    }
    
    return 0;
}