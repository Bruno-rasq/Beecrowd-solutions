#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main(){

    string data;

    while(getline(cin, data)){

        stringstream ss(data);
        string dd, mm, yy;

        getline(ss, dd, '/');
        getline(ss, mm, '/');
        getline(ss, yy, '/');
        

        cout << mm << "/" << dd << "/" << yy << endl;
        cout << yy << "/" << mm << "/" << dd << endl;
        cout << dd << "-" << mm << "-" << yy << endl;
    }

    return 0;
}