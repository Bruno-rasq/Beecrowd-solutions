#include <iostream>
using namespace std;

int Distance2(int xi, int yi, int xf, int yf){
    int dx = xf - xi;
    int dy = yf - yi;
    return dx * dx + dy * dy;
}

int main() {
    int testCases;
    cin >> testCases;
    while (testCases--) {
        int N;
        int xi, yi; // branca
        cin >> N;
        cin >> xi >> yi;
        int xf, yf;
        cin >> xf >> yf; // bola 1
        int ans = 1;
        int minDist = Distance2(xi, yi, xf, yf);
        for (int i = 2; i <= N; i++) {
            cin >> xf >> yf;
            int dist = Distance2(xi, yi, xf, yf);
            if (dist < minDist) {
                minDist = dist;
                ans = i;
            }
        }
        cout << ans << '\n';
    }
}