#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

// Há N tiras de papel de 1cm de largura por X centímetros de
// altura. O programa pede para achar uma altura M tal que se
// corta as tiras de papel a sobra superior tenha uma area Y.

double superiorArea(const vector<int>& stripsHeights, double cut){
    double area = 0.0;

    for(const int& currentHeight: stripsHeights){
        if(cut <= currentHeight)
            // area de um retângulo (B * H), em que B = 1.
            area += currentHeight - cut;
    }

    return area;
}

int main() {

    int Nstrips, expectedArea;

    while(cin >> Nstrips >> expectedArea){

        if(Nstrips == 0 && expectedArea == 0)
            break;

        int maxHeight = 0;

        vector<int> stripsHeights(Nstrips, 0);

        for(size_t i = 0; i < stripsHeights.size(); i++){
            cin >> stripsHeights[i];
            maxHeight = max(maxHeight, stripsHeights[i]);
        }

        double area = superiorArea(stripsHeights, 0);

        if(area == expectedArea){
            cout << ":D\n";
            continue;
        }

        if(area < expectedArea){
            cout << "-.-\n";
            continue;
        }

        double left = 0.0;
        double right = maxHeight;

        while(right - left > 1e-7){

            double mid = (left + right) / 2.0;
            area = superiorArea(stripsHeights, mid);

            if(area > expectedArea)
                left = mid;
            else
                right = mid;
        }

        double ans = (left + right) / 2.0;

        cout << fixed << setprecision(4) << ans << "\n";
    }

    return 0;
}