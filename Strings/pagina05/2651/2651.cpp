#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    string input;
    getline(cin, input);

    transform(input.begin(), input.end(), input.begin(), ::tolower);

    cout << (input.find("zelda") != string::npos ? "Link Bolado" : "Link Tranquilo") << endl;

    return 0;
}