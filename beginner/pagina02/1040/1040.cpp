#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    float n1, n2, n3, n4;
    cin >> n1 >> n2 >> n3 >> n4;

    float media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10;

    cout << "Media: " << fixed << setprecision(1) << media << endl;

    if (media >= 7.0){

        cout << "Aluno aprovado." << endl;
    }
    else if (media < 5.0){

        cout << "Aluno reprovado." << endl;
    }
    else{
        float exame, mediaComExame;
        cin >> exame;

        cout << "Aluno em exame." << endl;
        cout << "Nota do exame: " << exame << endl;

        mediaComExame = (media + exame) / 2;

        if (mediaComExame >= 5.0){
            cout << "Aluno aprovado." << endl;
        }
        else{
            cout << "Aluno reprovado." << endl;
        }

        cout << "Media final: "  << fixed << setprecision(1) << mediaComExame << endl;
    }

    return 0;
}