#include <iostream>

using namespace std;

int main(){
    int possibilidades[14] = {
        0, 6, 12, 90, 360, 2040, 10080, 54810, 290640, 
        1588356, 8676360, 47977776, 266378112, 1488801600
    };
    
    int n, curr;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> curr;
        cout << possibilidades[curr - 1] << endl;
    }
}