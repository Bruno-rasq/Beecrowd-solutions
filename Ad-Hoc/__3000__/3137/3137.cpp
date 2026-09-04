#include <iostream>

using namespace std;

int main(){

    int casas[7] = {1000000, 100000, 10000, 1000, 100, 10, 1};
    int n, total = 0;

    cin >> n;

    for(const int& casa : casas){
        if(n >= casa){
            int qnt = n - casa + 1;
            int digitos = to_string(casa).size();
            total += qnt * digitos;
            n = casa - 1;
        }
    }

    cout << total << endl;

    return 0;
}