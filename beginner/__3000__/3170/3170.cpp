#include <iostream>

using namespace std;

int main(){

    int b, g;
    cin >> b >> g;

    int result = (g/2) - b;

    if(result <= 0){
        cout << "Amelia tem todas bolinhas!" << endl;
    } else {
        cout << "Faltam " << result << " bolinha(s)!" << endl;
    }

    return 0;
}