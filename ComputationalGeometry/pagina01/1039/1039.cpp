#include <iostream>
#include <cmath>
using namespace std;

bool fire_flowers(int r1, int x1, int y1, int r2, int x2, int y2){
    double distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
    return distancia <= (r1 - r2);
}

int main() {
    int r1, int x1, int y1, int r2, int x2, int y2

    while ( cin >> r1 >> x1 >> y1 >> r2 >>  x2 >> y2 ){
        if(fire_flowers(r1, x1, y1, r2, x2, y2)){
            cout << "RICO" << endl;
            continue;
        }

        cout << "MORTO" << endl;
    }
    return 0;
}