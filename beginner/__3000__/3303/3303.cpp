#include <iostream>

using namespace std;

int mani(){

    string palavra;
    cin >> palavra;

    if(palavra.size() >= 10){
        cout << "palavrao" << endl;
    } else {
        cout << "palavrinha" << endl;

    }

    return 0;
}