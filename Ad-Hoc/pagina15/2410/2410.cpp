#include <iostream>
#include <map>

using namespace std;

int main(){
    map<int, bool> notas;
    int N, curr;

    cin >> N;
    for(int i = 0; i < N; i++){
        cin >> curr;
        notas[curr] = true;
    }

    cout << notas.size() << endl;

    return 0;
}