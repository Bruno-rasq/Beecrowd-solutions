#include <iostream>

using namespace std;

int main(){
    int e, g, f, count = 0;
    cin >> e >> g >> f;

    e = e + g;
    while(e >= f){
        e = (e - f + 1);
        count++;
    }

    cout << count << endl;
    
    return 0;
}