#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    double a, b, c;
    cin >> a >> b >> c;
    
    double tempo = (a * b * c) / (a * b + a * c + b * c);
    cout << fixed << setprecision(3) << tempo << endl;
}