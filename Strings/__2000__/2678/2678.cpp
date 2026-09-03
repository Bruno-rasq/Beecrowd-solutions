#include <iostream>
#include <unordered_map>
#include <cctype>
using namespace std;

int main() {
    unordered_map<char, char> nokia_keyboard = {
        {'a', '2'}, {'b', '2'}, {'c', '2'},
        {'d', '3'}, {'e', '3'}, {'f', '3'},
        {'g', '4'}, {'h', '4'}, {'i', '4'},
        {'j', '5'}, {'k', '5'}, {'l', '5'},
        {'m', '6'}, {'n', '6'}, {'o', '6'},
        {'p', '7'}, {'q', '7'}, {'r', '7'}, {'s', '7'},
        {'t', '8'}, {'u', '8'}, {'v', '8'},
        {'w', '9'}, {'x', '9'}, {'y', '9'}, {'z', '9'}
    };

    string input;
    while (getline(cin, input)) {
        string output = "";

        for (char chr : input) {
            if (isalpha(chr)) {
                // converte para minúscula e busca no mapa
                output += nokia_keyboard[tolower(chr)];
            } else if (isdigit(chr) || chr == '*' || chr == '#') {
                output += chr;
            }
            // outros símbolos são ignorados
        }

        cout << output << endl;
    }

    return 0;
}