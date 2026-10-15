#include <iostream>
#include <sstream>
using namespace std;

// DADO UM VALOR N, CRIAR UMA MATRIZ QUADRADA NxN de 'o' COM UM
// 'X' QUE INICIA NO CENTRO E FAZ UMA ESPIRAL ATÉ O FINAL DA MATRIZ
// NO SENTIDO ANTI-HORARIO. DEVE EXIBIR TODOS OS ESTÁGIOS DE MOVIMENTO.

void printStep(const int n, int pos_x, int pos_y){
    stringstream buffer;
    for(int row = 0; row < n; row++){
        for(int col = 0; col < n; col++)
            buffer << (row == pos_x && col == pos_y ? 'X' : 'O');
        buffer << '\n';
    }
    buffer << "@\n";
    cout << buffer.str();
}

int main() {
    int n;
    while (cin >> n && n != 0) {

        int pos_x = n / 2;
        int pos_y = n / 2;
        
        // Exibe o passo inicial no centro
        printStep(n, pos_x, pos_y);

        int passos_para_andar = 1;
        int passos_dados = 1; // Já contamos o ponto central
        int total_elementos = n * n;

        while (passos_dados < total_elementos) {
            
            for (int i = 0; i < passos_para_andar && passos_dados < total_elementos; i++) {
                pos_y++;
                printStep(n, pos_x, pos_y);
                passos_dados++;
            }

            for (int i = 0; i < passos_para_andar && passos_dados < total_elementos; i++) {
                pos_x--;
                printStep(n, pos_x, pos_y);
                passos_dados++;
            }

            passos_para_andar++;

            for (int i = 0; i < passos_para_andar && passos_dados < total_elementos; i++) {
                pos_y--;
                printStep(n, pos_x, pos_y);
                passos_dados++;
            }

            for (int i = 0; i < passos_para_andar && passos_dados < total_elementos; i++) {
                pos_x++;
                printStep(n, pos_x, pos_y);
                passos_dados++;
            }

            passos_para_andar++;
        }
    }
    return 0;
}
