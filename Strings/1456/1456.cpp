#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <map>

using namespace std;

void solve() {
    string input_data;
    string source_code;

    // ORDEM CORRETA
    cin >> input_data >> source_code;

    vector<unsigned char> memory(30000, 0);
    int ptr = 0;
    int input_idx = 0;

    // Precompute loop pairs
    map<int, int> loop_map;
    stack<int> s;

    for (int i = 0; i < (int)source_code.length(); i++) {
        if (source_code[i] == '[') {
            s.push(i);
        } else if (source_code[i] == ']') {
            int start = s.top();
            s.pop();
            loop_map[start] = i;
            loop_map[i] = start;
        }
    }

    // Execute Brainfuck
    for (int pc = 0; pc < (int)source_code.length(); pc++) {
        char cmd = source_code[pc];

        switch (cmd) {
            case '>': ptr++; break;
            case '<': ptr--; break;
            case '+': memory[ptr]++; break;
            case '-': memory[ptr]--; break;

            case '.':
                // PRINT COMO CHAR
                cout << (char)memory[ptr];
                break;

            case ',':
                if (input_idx < (int)input_data.length()) {
                    memory[ptr] = input_data[input_idx++];
                } else {
                    memory[ptr] = 0;
                }
                break;

            case '[':
                if (memory[ptr] == 0) {
                    pc = loop_map[pc];
                }
                break;

            case ']':
                if (memory[ptr] != 0) {
                    pc = loop_map[pc];
                }
                break;

            case '#':
                // PRIMEIROS 10 BYTES (SEM FILTRO)
                for (int i = 0; i < 10; i++) {
                    cout << (int)memory[i];
                }
                break;

            default:
                // ignora qualquer outro caractere
                break;
        }
    }

    cout << "\n";
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Instancia " << i << "\n";
        solve();
        cout << "\n"; // linha em branco obrigatória
    }

    return 0;
}