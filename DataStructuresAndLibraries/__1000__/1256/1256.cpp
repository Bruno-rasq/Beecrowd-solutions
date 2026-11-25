#include <iostream>
#include <vector>
#include <sstream>
using namespace std;


int main() {

    int n;
    cin >> n;
    stringstream buffer;

    for(size_t i = 0; i < n; i++){

        int base, values;
        cin >> base >> values;
        
        vector<vector<int>> hash(base);

        for(size_t j = 0; j < values; j++){
            int value;
            cin >> value;

            size_t key = (size_t) value % base;

            hash[key].push_back(value);
            
        }

        for(size_t key = 0; key < base; key++){
            buffer << key << " -> ";
            for(int& value : hash[key])
                buffer << value << " -> ";
            buffer << "\\\n";
        }

        if(i != (n - 1)) buffer << "\n";

    }
    
    cout << buffer.str();

    return 0;
}