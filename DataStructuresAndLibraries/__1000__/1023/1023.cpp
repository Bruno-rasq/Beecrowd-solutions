#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

using namespace std;

int main(){

    int n, t = 0;;
    cin >> n;

    while(n != 0){

        if(t){
            cout << "" << endl;
        }

        vector<int> consumos(201, 0);
        int totalX = 0, totalY = 0;

        for(int i = 0; i < n; i++){
            int x, y;
            cin >> x >> y;

            totalX += x;
            totalY += y;

            consumos[static_cast<int>[floor(static_cast<double>(y) / x)]] += x;
        }

        cout << "Cidade# " << ++t << ":\n";

        vector<string> output;
        for(int i = 0; i < 201; ++i){
            if(consumos[i] > 0){
                uotput.push_back(to_string(consumos[i]) + "-" + to_string(i))
            }
        }
        for(int i= 0; i < output.size(); +=i){
            if(i > 0) cout << " ";
            cout << output[i];
        }

        cout << endl;

        double consumoTotal = floor(100.0 * totalY / totalX) / 100.0;

        cout << "Consumo medio: " << fixed << setprecision(2) << consumoTotal << " m3." << endl;

        cin >> n;
    }

    return 0;
}