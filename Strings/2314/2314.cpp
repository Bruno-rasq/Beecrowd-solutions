#include <iostream>
#include <string>

using namespace std;

string indent(int deep, int indent_size = 4) {
    return string(deep * indent_size, '.');
}

string format_cpp_like(const string& code, int indent_size = 4) {
    int deep = 0;
    string out;
    bool new_line = true;

    int paren_depth = 0; // <<< CONTADOR SIMPLES

    for (char c : code) {

        // controle de parênteses
        if (c == '(') paren_depth++;
        else if (c == ')') {
            if (paren_depth > 0) paren_depth--;
        }

        if (c == '{') {
            if (!out.empty() && out.back() != '\n') out += '\n';
            out += indent(deep) + "{\n";
            deep++;
            new_line = true;
        }

        else if (c == '}') {
            if (!out.empty() && out.back() != '\n') out += '\n';
            if (deep > 0) deep--;
            out += indent(deep) + "}\n";
            new_line = true;
        }

        else if (c == ';') {
            out += ";";

            // <<< REGRA SIMPLES E CORRETA
            if (paren_depth == 0) {
                out += "\n";
                new_line = true;
            }
        }

        else {
            if (new_line) {
                out += indent(deep);
                new_line = false;
            }
            out += c;
        }
    }

    while (!out.empty() && out.back() == '\n')
        out.pop_back();

    return out;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string input, line;
    while (getline(cin, line)) {
        input += line + "\n";
    }

    cout << format_cpp_like(input, 4) << "\n";
    return 0;
}