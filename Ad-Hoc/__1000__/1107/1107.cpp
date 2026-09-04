#include <iostream>
#include <vector>
using namespace std;

// A ideia é somar todas as quedas de altura.
// Primeiro contamos a queda inicial (do topo até a primeira posição).
// Depois, para cada posição, se a altura for menor que a anterior,
// significa que o laser precisou ligar para descer, então somamos essa diferença.
int laser_sculture(int height, int length, vector<int>& heights) {
    int response = height - heights[0];  
    for (int i = 1; i < length; i++) {
        if (heights[i] < heights[i-1]) {
            response += heights[i-1] - heights[i];
        }
    }
    return response;
}

int main() {
    int height, length;
    while (cin >> height >> length) {
        if (height == 0 && length == 0) break;

        vector<int> heights(length);
        for (int i = 0; i < length; i++) {
            cin >> heights[i];
        }

        int out = laser_sculture(height, length, heights);
        cout << out << endl;
    }
    return 0;
}