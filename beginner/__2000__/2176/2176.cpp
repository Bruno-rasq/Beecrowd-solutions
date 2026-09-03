#include <iostream>

using namespace std;

int main(){

    string input;
    cin >> input;

    int bits_1 = 0;
    for(int i = 0; i < input.size(); i++){
        char bit = input[i];
        bits_1 += (bit == "1" ? 1 : 0);
    }

    if(bits_1 % 2 == 0){
        input += "0";
    } else {
        input += "1";
    }

    cout << input << endl;
    
    return 0;

}