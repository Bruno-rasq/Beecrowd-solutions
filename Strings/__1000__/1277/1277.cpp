#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef vector<string> VetStr;

void get(VetStr& lista, int n) {
    for (int j = 0; j < n; j++) {
        string data;
        cin >> data;
        lista.push_back(data);
    }
}

bool calcular_frequencia(int total, int faltas) {
    int presencas = total - faltas;
    float frequencia = (presencas * 100.0) / total;
    return frequencia >= 75.0;
}

int main() {
    int casos;
    cin >> casos;

    for (int i = 0; i < casos; i++) {
        int n_alunos;
        cin >> n_alunos;

        VetStr alunos;
        VetStr frequencias;
        VetStr alunos_baixa_frequencia;

        get(alunos, n_alunos);
        get(frequencias, n_alunos);

        for (int j = 0; j < n_alunos; j++) {
            string aluno = alunos[j];
            string frequen = frequencias[j];

            int total = 0;
            int faltas = 0;

            for (const char& f : frequen) {
                if (f == 'M') continue;
                if (f == 'A') faltas++;
                total++;
            }

            if (total > 0 && !calcular_frequencia(total, faltas)) {
                alunos_baixa_frequencia.push_back(aluno);
            }
        }

        for (size_t k = 0; k < alunos_baixa_frequencia.size(); ++k) {
            cout << alunos_baixa_frequencia[k];
            if (k != alunos_baixa_frequencia.size() - 1) cout << " ";
        }
        cout << endl;
    }

    return 0;
}