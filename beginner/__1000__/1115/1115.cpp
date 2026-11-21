#include <iostream>
#include <cstdint>
using namespace std;

int main() {

    int32_t x, y;

    while(cin >> x >> y && x != 0 && y != 0){
        if(x > 0 && y > 0) cout << "primeiro\n";
        if(x < 0 && y > 0) cout << "segundo\n";
        if(x < 0 && y < 0) cout << "terceiro\n";
        if(x > 0 && y < 0) cout << "quarto\n";
    }
    
    return 0;
}