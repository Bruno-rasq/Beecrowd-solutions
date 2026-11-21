#include <iostream>
using namespace std;

int main() {
    int min = 999999;
    int pos = -1;

    int T;
    cin >> T;
    for(size_t idx = 0; idx < T; idx++){
        int N;
        cin >> N;
        if(N < min){
            min = N;
            pos = idx;
        }
    }

    cout << "Menor valor: " << min << "\n";
    cout << "Posicao: " << pos << "\n";
    return 0;
}