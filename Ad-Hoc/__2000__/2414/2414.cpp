#include <iostream>
using namespace std;

// PEGAR O MAIOR VALOR EM UMA SEQUÊNCIA DE INTEIROS.
int main() {
    int n;
    int ans = 0;
    while(cin >> n && n != 0){
        if(n > ans)
            ans = n;
    }
    cout << ans << "\n";
    return 0;
}