#include <iostream>
#include <vector>
using namespace std;

/*
    lista com N elementos (inteiros), cada consulta recebe um indice
    left e right, e deve retornar a somatória de elementos nesse intervalo

    a ideia é para cada elementos guardar a somatória total até o mesmo
    assim a consulta vira apenas um calculo da somatória até Right - o que
    vinha antes de left.

    x = somatoria[right] - somatória[left - 1];
*/

int main() {
    int n, q;
    cin >> n >> q;

    int s = 0;
    vector<int> sums;
    for(size_t i = 0; i < n; i++){
        int qnt;
        cin >> qnt;
        sums.push_back(qnt + s);
        s += qnt;
    }

    for(size_t i = 0; i < q; i++){
        int left, right;
        cin >> left >> right;

        left-=1;
        right-=1;

        int ans = sums[right] - (left == 0 ? 0 : sums[left - 1]);
        cout << ans << "\n";
    }

    return 0;
}