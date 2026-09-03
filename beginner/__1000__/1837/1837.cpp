#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int x, y, quo = 0;
    cin >> x >> y;

    if((x > 0 && y > 0) || (x < 0 && y > 0)){
        quo = floor(static_cast<double>(x) / y);
    } else {
        quo = ceil(static_cast<double>(x) / y);
    }

    cout << quo << " " << (x - (y * quo)) << endl;
    return 0;
}