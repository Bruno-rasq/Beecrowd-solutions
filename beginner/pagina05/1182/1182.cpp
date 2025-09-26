#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    char OP;
    int column;
    int _qnt = 0;
    double _sum = 0.0;
    double curr = 0.0;
    double average, output;

    cin >> column;
    cin >> OP;

    for(size_t i = 0; i < 12; i++){
        for(size_t j = 0; j < 12; j++){
            cin >> curr;

            if(j == column){
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