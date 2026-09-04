#include <iostream>

using namespace std;

int main(){
    int nredes;
    cin >> nredes;
    
    int grid[101][101] = {0};
    for(size_t i = 0; i < nredes; i++){
        int xi, xf, yi, yf;
        cin >> xi >> xf >> yi >> yf;
        for(size_t x = xi; x < xf; x++)
            for(size_t y = yi; y < yf; y++)
                grid[x][y]++;
    }
    
    int area_total = 0;
    for (int x = 0; x <= 100; x++)
        for (int y = 0; y <= 100; y++) 
            if (grid[x][y] > 0)
                area_total++;
        
    cout << area_total << "\n";
    return 0;
}