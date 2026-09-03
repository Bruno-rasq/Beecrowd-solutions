#include <iostream>
using namespace std;

string fixText(string text) {
    string fixed = "";
    for (size_t i = 0; i < text.size(); i++) {
        char character = text[i];
        if (i < text.size() - 1) {
            char next = text[i + 1];
            if (character == ' ' && (next == '.' || next == ',')) continue;
        }
        fixed += character;
    }
    return fixed;
}

int main(){
    string input;
    while(getline(cin, input)){
        cout << fixText(input) << endl;
    }
    return 0;
}