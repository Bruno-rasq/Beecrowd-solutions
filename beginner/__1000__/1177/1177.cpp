#include <iostream>
using namespace std;

int main() {

    int T;
    cin >> T;

    int aux = 0;

    for(size_t idx = 0; idx < 1000; idx++){
        cout << "N[" << idx << "] = " << aux << "\n";
        aux = (aux + 1) % T;
    }
    
    return 0;
}