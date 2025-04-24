#include <iostream>
#include <string>

using namespace std;

int main() {
    string alien_vowel;

    while (getline(cin, alien_vowel)) {
        string frases;
        if (!getline(cin, frases)) break;  // <-- só entra se as duas linhas forem válidas

        int contador = 0;

        for (char chr : frases) {
            if (alien_vowel.find(chr) != string::npos) {
                contador++;
            }
        }

        cout << contador << endl;
    }

    return 0;
}
