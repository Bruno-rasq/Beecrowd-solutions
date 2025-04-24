#include <iostream>
#include <set>
#include <vector>
#include <cmath>

using namespace std;

int main(){

    int N, B;
    cin >> N >> B;
    while(N != 0 && B != 0){

        vector<int> bolas;
        for(int i = 0; i < B; i++){
            int bola;
            cin >> bola;
            bolas.push_back(bola);
        }

        set<int> possibilidades;
        possibilidades.insert(0);

        for(int i = 0; i < B; i++){
            for(int j = i + 1; j < B; j++){
                possibilidades.insert(abs(bolas[i] - bolas[j]));
            }
        }

        cout << (possibilidades.size() == N + 1 ? 'Y' : 'N') << endl;
        cin >> N >> B;
    }

    return 0;
}