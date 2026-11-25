#include <iostream>
#include <string>
using namespace std;

int main() {

    int n;
    cin >> n;

    cin.ignore();

    for(int i = 0; i < n; i++){

        string text;
        getline(cin, text);

        string out = "";
        int length = text.size() / 2;
        int left = length - 1;
        int right = text.size() - 1;

        for(int j = 0; j < length; j++){
            out += text[left--];
        }

        for(int j = 0; j < length; j++){
            out += text[right--];
        }

        cout << out << "\n";
    }

    return 0;
}