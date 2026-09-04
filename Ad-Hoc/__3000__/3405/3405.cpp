#include <iostream>
#include <cmath>

using namespace std;

int trailing_zeros(int n){
    int count = 0;
    while (n >= 5){
        n = floor(n / 5);
        count += n;
    }
    return count;
}

int main(){
    int n;
    cin >> n;
    cout << trailing_zeros(n) << endl;

    return 0;
}