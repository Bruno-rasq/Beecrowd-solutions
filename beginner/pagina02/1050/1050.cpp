#include <iostream>
#include <unordered_map>
using namespace std;

int main() {

    unordered_map<int , string> DDD;

    DDD[61] = "Brasilia\n";
    DDD[71] = "Salvador\n";
    DDD[11] = "Sao Paulo\n";
    DDD[21] = "Rio de Janeiro\n";
    DDD[32] = "Juiz de Fora\n";
    DDD[19] = "Campinas\n";
    DDD[27] = "Vitoria\n";
    DDD[31] = "Belo Horizonte\n";
    
    int numero;
    cin >> numero;
    if(DDD.find(numero) == DDD.end())
        cout << "DDD nao cadastrado\n";
    else 
        cout << DDD[numero];    
}