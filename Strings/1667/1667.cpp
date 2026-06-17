#include <iostream>
#include <sstream>
using namespace std;

const int LIMIT = 80;

void clear_buffer(ostringstream& buffer) {
    buffer.str("");
    buffer.clear();
}

void print_text_line(ostringstream& buffer) {
    cout << buffer.str() << '\n';
    clear_buffer(buffer);
}

void print_hr() {
    cout << string(LIMIT, '-') << '\n';
}

int main() {
    ostringstream buffer;

    int count_chars = 0;
    bool first_word = true;

    string word;
    while (cin >> word) {

        if (word == "<br>") {
            print_text_line(buffer);
            count_chars = 0;
            first_word = true;
            continue;
        }

        if (word == "<hr>") {

            // Só quebra a linha se ela possuir conteúdo
            if (count_chars > 0) {
                print_text_line(buffer);
                count_chars = 0;
                first_word = true;
            }

            print_hr();
            continue;
        }

        int needed = word.size();

        if (!first_word)
            needed++; // espaço antes da palavra

        if (count_chars + needed > LIMIT) {
            print_text_line(buffer);

            count_chars = 0;
            first_word = true;
        }

        if (!first_word) {
            buffer << ' ';
            count_chars++;
        }

        buffer << word;
        count_chars += word.size();

        first_word = false;
    }

    // última linha
    if (count_chars > 0)
        print_text_line(buffer);

    return 0;
}