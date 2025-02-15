#include <iostream>

using namespace std;

int main(){

    int a, b, resp = 0;
    cin >> a >> b;

    if( a > b ) resp = (24 - a) + b;
    else if ( a < b ) resp = b - a;
    else if ( a == b) resp = (24 - a) + b;

    cout << "O JOGO DUROU " + to_string(resp) + " HORA(S)" << endl;

    return 0;
}