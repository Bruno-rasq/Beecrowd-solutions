#include <iostream>

using namespace std;

int main(){

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        string curr;
        cin >> curr;

        if(curr == "P=NP"){
            cout << "skipped" << endl;
            continue;
        }

        int a, b;
        size_t pos = curr.find("+");
        a = stoi(curr.substr(0, pos));
        b = stoi(curr.substr(pos + 1));

        cout << a + b << endl;
    }
    return 0;
}