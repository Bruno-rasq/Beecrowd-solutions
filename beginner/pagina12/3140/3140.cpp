#include <iostream>
#include <string>

using namespace std;

int main(){

    bool tag =  false;
    string lines;

    while(getline(cinn, line)){
        if(line.find("<body>") != string::npos){
            tag = true
            continue
        }

        if(line.find("</body>") != string::npos){
            break
        }

        if(tag){
            cout << line << endl;
        }

    }
    
    return 0;
}