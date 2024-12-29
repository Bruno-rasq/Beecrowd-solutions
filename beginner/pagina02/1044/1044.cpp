#include <iostream>

using namespace std;

int main(){

    int a, b;
    cin >> a >> b;

    if(a < b){
        int temp = b;
        b = a;
        a = temp;
    }

    a % b == 0 ? cout << "Sao Multiplos" << endl : cout << "Nao sao Multiplos" << endl;
    
    return 0;
}