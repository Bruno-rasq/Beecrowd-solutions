#include <iostream>
using namespace std;

int main() {
    int pos, n;
    int value = -1;
    for(size_t idx = 1; idx <= 100; idx++){
        cin >> n;
        if(n > value){
            value = n;
            pos = idx;
        }
    }
    cout << value << "\n" << pos << "\n";
    return 0;
}