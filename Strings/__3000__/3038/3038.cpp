#include <iostream>
using namespace std;

int main(){
    string line;
    while(getline(cin, line)){
        string decrypt = "";

        for(int j = 0; j < line.size(); j++){
            if (line[j] == "@"){decrypt += 'a';}
            else if (line[j] == "&"){decrypt += 'e';}
            else if (line[j] == "!"){decrypt += 'i';}
            else if (line[j] == "*"){decrypt += 'o';}
            else if (line[j] == "#"){decrypt += 'u';}
            else {decrypt += line[j];}
        }

        cout << decrypt << endl;
    }
    return 0;
}