#include <iostram>

#define dias_por_mes 30

using namespace std;

int  main(){

    int meses, velas_por_mes, resultado;
    cin >> meses >> velas_por_mes;

    resultado = (meses * dias_por_mes) * velas_por_mes;

    cout << resultado << endl;
    
    return 0;
}