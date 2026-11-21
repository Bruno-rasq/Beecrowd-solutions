#include <iostream>
using namespace std;

int main() {

    int pos = 0;
    for(size_t i = 0; i < 6; i++){
        float input;
        cin >> input;
        pos += (input >= 0.0) ? 1 : 0;
    }

    cout << pos << " valores positivos\n";

    return 0;
}