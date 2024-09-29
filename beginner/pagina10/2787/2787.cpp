#include <iostream>

using namespace std;

bool isEven(int num){
    return num % 2 == 0;
}

int main(){

    int l, c;
    cin >> l >> c;

    if( (isEven(l) && isEven(c)) || (!isEven(l) && !isEven(c)) ){
        cout << 1 << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}