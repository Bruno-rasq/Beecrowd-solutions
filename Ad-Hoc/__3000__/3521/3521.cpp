#include <iostream>
#include <queue>
using namespace std;

// X -> QUANTIDADE DE ENERGIA.
// N -> QUANTIDADE DE PETISCOS.
// K -> QUANTIDADE DE PILULAS.
//
// PETISCOS NEGATIVOS SÃO GUARDADOS EM UMA MIN-HEAP.
// QUANDO FOR NECESSÁRIO USAR UMA PILULA, ELA ANULA
// O PETISCO QUE MAIS PREJUDICOU A ENERGIA.

int main() {
    long long X;
    int N, K;

    cin >> X >> N >> K;

    priority_queue<long long, vector<long long>, greater<long long>> pq;

    int count = 0;

    for (int i = 0; i < N; i++) {
        long long petisco;
        cin >> petisco;

        X += petisco;

        if (petisco < 0)
            pq.push(petisco);

        // BELLA MORRERIA.
        if (X <= 0) {
            if (K == 0)
                break;

            // ANULA O PIOR PETISCO QUE JÁ COMEU.
            X -= pq.top();
            pq.pop();

            K--;
        }

        count++;
    }

    cout << count + 1 << '\n';

    return 0;
}