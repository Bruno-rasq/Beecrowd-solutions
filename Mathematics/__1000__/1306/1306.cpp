#include <iostream>
using namespace std;

int min_sufix(int ts, int ia){
    if(ts <= ia) return 0;
    ts -= ia; // reduz os valores alocados sem sufixo
    int loops = (ts + ia - 1) / ia; // loops == sufixos minimos
    if(loops > 26) return -1;
    return loops;
}

int main() {
    int tc = 0; //teste case 
    int ts, ia; // total_streets, integers_allocated
    while(cin >> ts >> ia){
        if (ts == 0 && ia == 0) break;
        tc++;
        int out = min_sufix(ts, ia);
        if(out == -1){ // precisou de mais de 26 sufixos
            cout << "Case " << tc << ": impossible\n";
            continue;
        }
        cout << "Case " << tc << ": " << out << "\n";
    }
}