#include <iostream>
#include <vector>

using namespace std;

float repeticoes_maxima(int peso, int reps) {
    return peso * (1 + (float(reps) / 30));  // Garantir que a divisão seja feita com float
}

float media_geral(vector<float>& medias) {
    float soma = 0;  // Inicializar a soma com 0
    for (const float& media : medias)
        soma += media;

    return soma / medias.size();
}

int main() {
    vector<float> medias;
    int w1, w2, reps;

    while (cin >> w1 >> w2 >> reps) {
        if (w1 == 0 && w2 == 0 && reps == 0)
            break;

        float w1_max = repeticoes_maxima(w1, reps);  // Garantir que o cálculo de repetição máxima seja float
        float w2_max = repeticoes_maxima(w2, reps);
        float media_rm = (w1_max + w2_max) / 2.0;

        medias.push_back(media_rm);

        if (1 <= media_rm && media_rm < 13) {
            cout << "Nao vai da nao" << endl;
        } else if (13 <= media_rm && media_rm < 14) {
            cout << "E 13" << endl;
        } else if (14 <= media_rm && media_rm < 40) {
            cout << "Bora, hora do show! BIIR!" << endl;
        } else if (40 <= media_rm && media_rm <= 60) {
            cout << "Ta saindo da jaula o monstro!" << endl;
        } else {
            cout << "AQUI E BODYBUILDER!!" << endl;
        }
    }

    float media = media_geral(medias);

    if (media > 40.0) {
        cout << "" << endl;
        cout << "Aqui nois constroi fibra rapaz! Nao e agua com musculo!" << endl;
    }

    return 0;
}
