#include <iostream>
using namespace std;

int main(){

    string n;
    cin >> n;

    if (n.find("13") != string::npos){
        cout << n << " es de Mala Suerte" << endl;
    }
    else{ cout << n << " NO es de Mala Suerte" << endl; }

    return 0;
}