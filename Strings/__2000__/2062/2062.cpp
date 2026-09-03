#include <iostream>
using namespace std;

int main(){

    int n;
    cin >> n;

    string correct_words = "";
    for(int i = 0; i < n; i++){
        string word;
        cin >> word;

        if(!correct_words.empty()){ correct_words += " "; }

        if(word.size() == 3){
            if(word.compare(0, 2, "OB") == 0){
                correct_words += "OBI";
                continue;
            }
            if(word.compare(0, 2, "UR") == 0){
                correct_words += "URI";
                continue;
            }
        } 
            
        correct_words += word;

    }

    cout << correct_words << endl;
    return 0;
}