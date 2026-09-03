#include <iostream>
#include <cmath>
#include <string>

using namespace std;

int main(){
    string line;
    while(getline(cin, line)){
        try {
            int n = stoi(line)
            if(n > 0){
                int result = static_cast<int>(log2(n));
                cout << result << endl;
            }
        } 
        catch (const invalid_argument){ continue; }
        catch (const out_of_range& e){ continue; }
    }
    return 0;
}