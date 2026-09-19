#include <iostream>
#include <sstream>
#include <algorithm> // Necessário para o sort e max/min

using namespace std;

void RESOLVE_TRINCA(stringstream& buffer, int A){
    if (A == 13) {
        buffer << "*\n";
    } else {
        buffer << (A + 1) << " " << (A + 1) << " " << (A + 1) << "\n";
    }
}

void RESOLVE_PAR(stringstream& buffer, int par, int diff){
    // Incrementa a carta diferente
    diff++;
    
    // Se ao incrementar ela virar igual ao par, pula para a próxima
    if (diff == par) {
        diff++;
    }
    
    // Se a carta diferente passou de 13, significa que precisamos subir o par
    if (diff > 13) {
        par++;
        diff = 1;
        // Se o par subiu e passou de 13, vira a menor trinca
        if (par > 13) {
            buffer << "1 1 1\n";
            return;
        }
    }
    
    // Garante a impressão em ordem crescente
    if (par < diff) {
        buffer << par << " " << par << " " << diff << "\n";
    } else {
        buffer << diff << " " << par << " " << par << "\n";
    }
}

int main() {
    ios_base::sync_with_stdio(false); // Otimização de I/O
    cin.tie(NULL);

    stringstream buffer;
    int cartas[3];

    while ((cin >> cartas[0] >> cartas[1] >> cartas[2]) && (cartas[0] != 0)) {
        // Ordena para facilitar a identificação
        sort(cartas, cartas + 3);

        if (cartas[0] == cartas[2]) { 
            // Todas iguais -> TRINCA
            RESOLVE_TRINCA(buffer, cartas[0]);
        }
        else if (cartas[0] == cartas[1]) { 
            // Par nos menores (ex: 5 5 8) -> par = cartas[0], diff = cartas[2]
            RESOLVE_PAR(buffer, cartas[0], cartas[2]);
        }
        else if (cartas[1] == cartas[2]) { 
            // Par nos maiores (ex: 3 8 8) -> par = cartas[1], diff = cartas[0]
            RESOLVE_PAR(buffer, cartas[1], cartas[0]);
        }
        else { 
            // Cartas todas diferentes -> SET
            buffer << "1 1 2\n"; 
        }
    }

    cout << buffer.str();
    return 0;
}
