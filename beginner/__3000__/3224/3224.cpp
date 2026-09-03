#include <iostream>

using namespace std;

int main(){

    string john, medico;
    cin >> john >> medico;

    if(john.size() >= medico.size())
        cout << "go" << endl;

    else
        cout << "no" << endl;
        
    return 0;
}