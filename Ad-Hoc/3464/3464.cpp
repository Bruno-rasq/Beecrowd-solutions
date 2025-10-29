#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int width, height, amount_sensors, sum = 0;
    cin >> width >> height >> amount_sensors;
    
    while (amount_sensors--) {
        int X, Y, radius;
        cin >> X >> Y >> radius;
        
        int i  = max(X - radius, 1);
        int j  = max(Y - radius, 1);
        int i2 = min(X + radius, width);
        int j2 = min(Y + radius, height);
        
        sum += (i2 - i + 1) * (j2 - j + 1);
    }
    
    cout << fixed << setprecision(0) << (sum /  (width * height)) << endl;
    return 0;
}