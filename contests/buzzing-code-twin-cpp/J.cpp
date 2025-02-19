#include <iostream>
using namespace std;
typedef unsigned long long LONG;

int main(){

    LONG a, b;
    while(cin >> a >> b){
        LONG result = a ^ b;
        cout << result << endl;
    }

    return 0;
}