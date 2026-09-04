#include <iostream>
using namespace std;

int steps(int n, int k){
     if(n == 1) return 0;
    return (steps(n - 1, k) + k) % n;
}

int main () {

    int n, a, b;
    cin >> n;

    for(int i = 0; i < n; i++){

        cin >> a >> b;
        int step = steps(a, b);
        cout << "Case " + to_string(i + 1) + ": " + to_string(step + 1) << endl;
    }
    return 0;
}