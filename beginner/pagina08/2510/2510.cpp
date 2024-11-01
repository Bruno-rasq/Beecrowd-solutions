#include <iostream>
#include <vector>

using namespace std;

int main() {

    int n;
    cin >> n;

    vector<string> villains;

    for(int i = 0; i < n; i++){
        string villain;
        getline(cin, villain);

        auto found = find(villans.begin(), villains.end(), villain);

        if(found == villains.end()){
            villains.push_back(villain);
            cout << "Y" << endl;
        } else {
            cout << "N" << endl;

        }

    }
    return 0;
}