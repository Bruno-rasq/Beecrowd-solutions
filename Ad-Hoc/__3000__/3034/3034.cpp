#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false; // 0 e 1 não são primos
    // Testa divisores de 2 até a raiz quadrada de n
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false; // Divisível, logo não é primo
        }
    }
    return true; // É primo
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        N++;
        bool ans = false;
        
        if(N % 7 == 0 && N % 2 != 0 && isPrime(N + 2)) ans = true;
        
        cout << (ans ? "Yes\n" : "No\n");
    }
} 