#include <iostream>

using namespace std;

int main(){
    string text;
    cin >> text;

    if(text.size(0) <= 140){
        cout << "TWEET" << endl;
    } else {
        cout << "MUTE" << endl;
    }
    
    return 0;
}