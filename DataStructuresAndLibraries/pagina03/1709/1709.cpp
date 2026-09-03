#include <iostream>
#include <cmath>
using namespace std;

int new_position(int pos, int n){
    int mid = ceil(n / 2);
    if(pos < mid) return pos * 2 + 1;
    return (pos - mid) * 2;
}

int main() {
    int n;
    int steps = 1, pos = 1;
    cin >> n;

    int aux = new_position(pos, n);
    while(aux != pos){
        steps++;
        aux = new_position(aux, n);
    }

    cout << steps << "\n";
    return 0;
}