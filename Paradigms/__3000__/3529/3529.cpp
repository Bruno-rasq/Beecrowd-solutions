#include <iostream>
#include <map>
#include <sstream>
using namespace std;

/*
    Uma universidade disponibilizou dois cursos, os alunos podem
    optar por se matricular no curso A, no curso B ou em ambos.

    o problema pede o todos codigos de matriculas em ordem e quantos
    alunos se maricularam em ambos.
*/

void Signs(map<int, int>& signs, int N){
    for(int i = 0; i < N; i++){
        int code;
        cin >> code;
        signs[code]++;
    }
}

int main() {

    map<int, int> signs;

    int N, M;
    cin >> N >> M;

    Signs(signs, N);
    Signs(signs, M);

    stringstream buffer;
    int ans = 0;

    for(const auto& [code, courses] : signs){
        if(courses > 1) ans++;
        if(buffer.tellp() > 0) buffer << " ";
        buffer << code;
    }

    cout << buffer.str() << "\n";
    cout << ans << "\n";

    return 0;
}

