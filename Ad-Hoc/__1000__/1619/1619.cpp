
#include <cstdio>
#include <cstdlib>
using namespace std;

bool bissexto(int ano){
    return (ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0);
}

const int DC[12] = {0, 31, 59, 90, 120, 151,181, 212, 243, 273, 304, 334};
const int DCB[12] = {0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335};

long long total_dias(int ano, int mes, int dia){
    long long total = 0;

    // anos completos anteriores
    total += (long long)(ano - 1) * 365;
    total += (ano - 1) / 4;
    total -= (ano - 1) / 100;
    total += (ano - 1) / 400;

    // dias do ano atual
    if(bissexto(ano))
        return total + DCB[mes - 1] + dia;
    return total + DC[mes - 1] + dia;
}

int main() {
    int n;
    scanf("%d", &n);
    
    while(n--){
        int ya, ma, da, yb, mb, db;
        scanf("%d-%d-%d %d-%d-%d", &ya, &ma, &da, &yb, &mb, &db);
        
        long long total_abs_a = total_dias(ya, ma, da);
        long long total_abs_b = total_dias(yb, mb, db);
        
        int out = llabs(total_abs_a - total_abs_b); 
        printf("%lld\n", out);
    }
}