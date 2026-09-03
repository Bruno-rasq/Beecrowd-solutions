#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    float A, B, C;
    cin >> A >> B >> C;

    float perimetro = (A + B + C);
    float area = ((A + B) * C ) / 2;
    bool condicao = A < (B + C) && B < ( A + C) && C < (A + B);

    if(condicao){
        cout << "Perimetro = " <<  fixed << setprecision(1) << perimetro << endl;
    } else {
        cout << "Area = " << fixed << setprecision(1) << area << endl;
    }

    return 0;
}