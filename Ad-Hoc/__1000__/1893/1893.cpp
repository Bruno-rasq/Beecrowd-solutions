#include <iostream>

using namespace std;

int main() {

    int porcent1, porcent2;
    cin >> porcent1 >> porcent2;

    if ( porcent2 <= 2 && porcent2 >= 0 )
        cout << "nova" << endl;

    else if ( porcent2 <= 100 && porcent2 >= 97 )
        cout << "cheia" << endl;

    else if ( porcent1 < porcent2)
        cout << "crescente" << endl;

    else 
        cout << "minguante" << endl; 

    return 0;
}