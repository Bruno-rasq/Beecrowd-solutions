#include <iostream>

using namespace std;

int main(){

    string traces, traces2 = "|";

    for(int i = 0; i < 39; i++){
        traces += "-";
    }

    
    for(int i = 0; i < 37; i++){
        traces2 += " ";
    }

    traces2 += "|";

    cout << traces << endl;

    cout << traces2 << endl;
    cout << traces2 << endl;
    cout << traces2 << endl;
    cout << traces2 << endl;
    cout << traces2 << endl;

    cout << traces << endl;

    return 0;
}