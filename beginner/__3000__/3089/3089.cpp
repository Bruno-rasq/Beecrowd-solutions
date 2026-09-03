#include <iostream>
#include <vector>

using namespace std;

int main(){

    while(true){

        vector<int> presentes;
        vector<int> pares;
        int n;

        cin >> n;
        
        if(n == 0){
            break;
        }

        for(int i = 0; i < 2 * n; i++){
            int curr;
            cin >> curr;
            presentes.push_back(curr);
        }

        for(int i = 0; i < n; i++){
            pares.push_back(presentes[i] + presentes[2 * n - i - 1]);
        }

        int max = pares[0];
        int min = pares[0];

        for(int i = 1; i < n; i++){
            if(pares[i] > max)
                max = pares[i];
            if(pares[i] < min)
                min = pares[i];
        }

        cout << max << " " << min << endl;

    }
    return 0;
}