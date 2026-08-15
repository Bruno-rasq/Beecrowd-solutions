#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <functional>
using namespace std;

// FUNÇÃO DE OPERAÇÃO QUE RECEBE UM VALOR E RETORNA O VALOR COM OS
// DIGITOS INVERTIDOS IGNORANDO OS ZEROS A ESQUERDA.
int INVERT(int num) {
    int inverted = 0;

    while (num > 0) {
        int digit = num % 10;
        inverted = (inverted * 10) + digit;
        num /= 10;
    }

    return inverted;
}

int INCREMENT(int num) {
    return num + 1;
}

// CARROSSEL DE FUNÇÕES PARA FACILITAR A ESCRITA DO CÓDIGO.
const vector<function<int(int)>> OPERATIONS = {
    INCREMENT,
    INVERT
};

// ETAPAS DO PROCESSAMENTO DA RESPOSTA.
struct Step {
    int value;
    int steps;
};

int BFS(int source, int target) {
    queue<Step> steps;
    unordered_map<int, bool> visiteds;

    steps.push({source, 0});
    visiteds[source] = true;

    while (!steps.empty()) {
        Step currStep = steps.front();
        steps.pop();

        if (currStep.value == target)
            return currStep.steps;

        for (function<int(int)> func : OPERATIONS) {
            int nextValue = func(currStep.value);

            if (!visiteds[nextValue]) {
                visiteds[nextValue] = true;
                steps.push({nextValue, currStep.steps + 1});
            }
        }
    }

    return -1;
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int source, target;
        cin >> source >> target;

        cout << BFS(source, target) << "\n";
    }

    return 0;
}