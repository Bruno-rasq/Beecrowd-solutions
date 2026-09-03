#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int index = 0;
    string curr;

    vector<string> data;

    getline(cin, curr);
    data.push_back(curr);

    getline(cin, curr);
    data.push_back(curr);

    getline(cin, curr);
    data.push_back(curr);

    for(int i = 0; i < 3; i++){
        string A = data[index];
        string B = data[(index + 1) % data.size()];
        string C = data[(index + 2) % data.size()];

        cout << "A = " << A << ", B = " << B << ", C = " << C << endl;
        index = (index + 1) % data.size();
    }

    return 0;
}