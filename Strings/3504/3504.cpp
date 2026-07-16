#include <bits/stdc++.h>
using namespace std;

int main() {
    string sentense;
    getline(cin, sentense);

    size_t ptr1 = 0;
    size_t ptr2 = sentense.size() - 1;
    bool ispalindrome = true;
    while (ptr1 != ptr2) {
        if(sentense[ptr1] != sentense[ptr2]){
            ispalindrome = false;
            break;
        }
        ptr1++;
        ptr2--;
    }

    if (ispalindrome) cout << "A frase [" << sentense << "] eh palindrome\n";
    else cout << "A frase [" << sentense << "] nao eh palindrome\n";

    return 0;
}