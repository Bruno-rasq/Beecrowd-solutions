#include <iostream>
#include <sstream>
using namespace std;

int main(){
    stringstream buffer;
    
    int test_case;
    int test_num = 1;
    while(true){
        
        cin >> test_case;
        if(test_case == 0) break;
        
        int aldo = 0, beto = 0;
        int num1, num2;
        for(size_t i = 0; i < test_case; i++){
            cin >> num1 >> num2;
            aldo += num1;
            beto += num2;
        }
        
        buffer << "Teste " << test_num << "\n";
        buffer << (aldo > beto ? "Aldo" : "Beto") << "\n";
        buffer << "\n";
        test_num++;
    }
    
    cout << buffer.str();
    
    return 0;
}