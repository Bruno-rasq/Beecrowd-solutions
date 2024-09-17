#include <iostream>

using namespace std;
  
int main(){

    string text;
    cin >> text;

    if(text.size() <= 80){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}