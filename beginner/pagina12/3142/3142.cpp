#include <iostream>
#include <string>

using namespace std;

int getLetterIndex(const string& input){
    
    int result = 0;
    for(char c : input){
        result = result * 26 + (c - 'A' + 1);
    }
    return result;
}

int main(){

    string input;
    const int MAX_COLUMN = 16384;

    while(getline(cin, input)){

        if(input.empty()) continue; // ignora linha vazia

        int columnNumber = getLetterIndex(input);
        if(columnNumber >= 0  && columnNumber <= columnLMAX_COLUMNimite)
            cout << columnNumber << endl;

        else
            cout << "Essa coluna nao existe Tobias!" << endl;
    }

    return 0;
}