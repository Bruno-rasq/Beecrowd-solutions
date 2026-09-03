#include <iostream>
#include <string>
using namespace std;

int main() {
     
     int n;
     cin >> n;

    int guardachuvaCasa = 0;
    int guardachuvatrabalho = 0;
    int comprasCasa = 0;
    int comprasTrabalho = 0;

    string ida, volta;

     for(int i = 0; i < n; i++){
        cin >> ida >> volta;

        if(ida == "chuva"){
            guardachuvaCasa > 0 ? guardachuvaCasa-- : comprasCasa++;
            guardachuvatrabalho++;
        }

        if(volta == "chuva"){
            guardachuvatrabalho > 0 ? guardachuvatrabalho-- : comprasTrabalho++;
            guardachuvaCasa++;
        }
     }

     cout << to_string(comprasCasa) + " " + to_string(comprasTrabalho) << endl;
     return 0;
}