#include <iostream>
#include <sstream>
using namespace std;

int main() {

    int even = 0, odd = 0;
    ostringstream evenArr;
    ostringstream oddArr;

    for(size_t idx = 0; idx < 15; idx++){
        int input;
        cin >> input;
        
        if(input % 2 == 0){
            evenArr << "par[" << even << "] = " << input << "\n";
            even++;
            if(even == 5){
                cout << evenArr.str();
                evenArr.str("");
                even = 0;
            }
        }
        else {
            oddArr << "impar[" << odd << "] = " << input << "\n";
            odd++;
            if(odd == 5){
                cout << oddArr.str();
                oddArr.str("");
                odd = 0;
            }
        }
    }

    if(odd != 0) cout << oddArr.str();
    if(even != 0) cout << evenArr.str();
    
    return 0;
}
