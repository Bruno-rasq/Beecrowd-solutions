#include <iostream>
#include <cmath>

using namespace std;

string crescimento_popucional(int PA, int PB,float GA, float GB){

    int response = 1;
    for(int i = 1; i < 101; i++){
        if (PA > PB)
            break;
        PA += int(PA * GA);
        PB += int(PB * GB);
        response += 1;
    }

    return (PA <= PB ) ? "Mais de 1 seculo" : to_string(response - 1) + " anos.";
}

int main(){

    int n;
    cin >> n;

    for(int i = 0; i < n; i++){
        int pa, pb;
        float ga, gb;

        cin >> pa >> pb >> ga >> gb;

        ga /= 100;
        gb /= 100;
        
        string crecimento = crescimento_popucional(pa, pb, ga, gb);

        cout << crecimento << endl;
    }
    return 0;
}