#include <iostream>
using namespace std;

int main() {

    string ans = "LIVRE";

    int prof_hora, prof_min;
    cin >> prof_hora >> prof_min;

    int limite = max(420, prof_hora * 60 + prof_min);

    for(int i = 0; i < 3; i++){

        int aluno_hora, aluno_minuto;
        cin >> aluno_hora >> aluno_minuto;

        int chegada = aluno_hora * 60 + aluno_minuto;

        if(chegada > limite)
            ans = "FUMO";
    }

    cout << ans << "\n";

    return 0;
}