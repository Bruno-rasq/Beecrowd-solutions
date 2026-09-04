#include <iostream>
using namespace std;

int main(){
    int i1, i2;
    cin >> i1 >> i2;

    bool condicao = ((i1 >= 14 && i2 >= 14) || (i1 >= 18 || i2 >= 18)) && i1 >= 6 && i2 >= 6;
    cout << (condicao ? "YES" : "NO") << endl;

    return 0;
}