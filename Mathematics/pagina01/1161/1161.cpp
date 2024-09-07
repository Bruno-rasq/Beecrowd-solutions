#include <iostream>

using namespace std;

long fatorial(int n){
    if(n == 1 || n == 0){
        return 1;
    }
    return n * fatorial(n - 1);
}

int main() {

    int a, b;
    while(cin >> a >> b){
        long fa = fatorial(a);
        long fb = fatorial(b);

        long soma = fa + fb;
        cout << soma << endl;
    }

    return 0;
}