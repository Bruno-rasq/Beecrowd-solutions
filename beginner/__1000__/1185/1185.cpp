#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    char OP;
    double _sum = 0.0;
    double curr = 0.0;
    double average, output;
    int _qnt = 0;

    cin >> OP;

    for(size_t i = 0; i < 12; i++){
        for(size_t j = 0; j < 12; j++){
            cin >> curr;

            if(j < 11 - i){
                _sum += curr;
                _qnt += 1;
            }
        }
    }

    average = _sum / _qnt;
    output = (OP == 'M') ? average : _sum;

    cout << fixed << setprecision(1) << output << endl;

    return 0;
}