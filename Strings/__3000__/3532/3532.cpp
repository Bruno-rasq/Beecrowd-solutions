#include <iostream>
using namespace std;

int main() {

    int n;
    cin >> n;
    for(size_t i = 0; i < n; i++){
        string word;
        cin >> word;

        char lastChar = word.at(word.size() - 1);

        if(lastChar == 'a' || lastChar == 'e' || lastChar == 'i'
          || lastChar == 'o' || lastChar == 'u')
            word += 'h';

        cout << word << "\n";
    }

    return 0;
}