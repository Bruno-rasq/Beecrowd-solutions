#include <iostream>
#include <vector>

using namespace std;

int main() {

    int total_pecas;
    vector<int> pecas;

    cin >> total_pecas;
    for(size_t i = 0; i < total_pecas; i++){
        int curr;
        cin >> curr;
        pecas.push_back(curr);
    }

    for(size_t i = 1; i <= total_pecas; i++){

        auto pos = find(pecas.begin(), pecas.end(), i);
        if(pos == pecas.end()){
            cout << i << endl;
            break;
        }
    }

    return 0;
}