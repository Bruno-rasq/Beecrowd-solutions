#include <iostream>
using namespace std;

int main() {
    int dias_treino;
    
    while (cin >> dias_treino) {
        float maior_media_velocidade = 0.0;
        
        for (int dia = 1; dia <= dias_treino; dia++) {
            int tempo, distancia;
            cin >> tempo >> distancia;

            // Cast explícito para evitar divisão inteira
            float media_velocidade = static_cast<float>(distancia) / tempo;
            
            if (media_velocidade > maior_media_velocidade) {
                maior_media_velocidade = media_velocidade;
                cout << dia << endl;
            }
        }
    }
    
    return 0;
}