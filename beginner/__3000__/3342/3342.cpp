#include <iostream>

using namespace std;

int main() {

    int n, b = 0, p = 0;
    cin >> n;

    int total_cases = n * n;

    if (n % 2 == 0){
        b = total_cases / 2;
        p = total_cases / 2;
    } else {
        b = (total_cases + 1) / 2;
        p = b - 1;
    }

    cout << to_string(b) << " casas brancas e " << to_string(p) << " casas pretas" << endl;

    return 0;
}