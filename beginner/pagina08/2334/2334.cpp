#include <iostream>
using namespace std;

int main(){

    unsigned long long n_patinhos;
    while (cin >> n_patinhos){

        if(n_patinhos == (unsigned long long)-1)  break;

        cout << (n_patinhos > 0 ? n_patinhos - 1 : 0) << endl;
    }
    return 0;
}