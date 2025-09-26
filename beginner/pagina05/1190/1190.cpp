#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    
    char OP;
    double _sum = 0.0;
    double curr = 0.0;
    size_t _qtn = 0;
    
    cin >> OP;
    
    for(size_t i = 0; i < 12; i++){
        for(size_t j = 0; j < 12; j++){
            cin >> curr;
            
            bool conditiontop = (i < 6 && j > 11 - i);
            bool conditionbottom = (i > 5 && j > i);
            
            if(conditiontop || conditionbottom){
                _sum += curr;
                _qtn += 1;
            }
        }
    }
    
    double average = _sum / _qtn;
    double output = (OP == 'M') ? average : _sum;
    
    cout << fixed << setprecision(1) << output << endl;
    
    
    return 0;
}