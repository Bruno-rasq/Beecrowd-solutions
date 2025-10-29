#include <iostream>
#include <cmath>
#include <string> // necessário para std::to_string

long long qnt_edges(long long FP, long long FH)
{
    // Formula -> E = (5 * qnt faces pentagonais + 6 * qnt faces hexagonais ) / 2
    long long edges = (5 * FP + 6 * FH) / 2;
    return edges;
}

long long qnt_nodes(long long FP, long long FH, long long E)
{
    // Fórmula de Euler: F + V = E + 2  → V = E + 2 - F
    long long faces = FP + FH;
    long long nodes = E + 2 - faces;
    return nodes;
}

int main()
{
    int iter = 1;
    long long FP, FH, E, N;
    
    while (std::cin >> FP >> FH)
    {
        E = qnt_edges(FP, FH);
        N = qnt_nodes(FP, FH, E);
        
        std::cout << "Molecula #" << iter << ".:.\n";
        std::cout << "Possui " << N << " atomos e " << E << " ligacoes\n";
        std::cout << "\n";
        
        iter++;
    }
    
    return 0;
}