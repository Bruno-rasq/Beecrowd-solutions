#include <iostream>
using namespace std;

// Exibir mensagem pré programada de acordo com a quantidade usada de espaço
// do disco rigido no servidor. 

int main(){
    const string warning = "warning", critical = "critical", ok = "OK";
    int total_harddisk_size, used, war_percent, cri_percent;
    while(cin >> total_harddisk_size >> used >> war_percent >> cri_percent){
        int percent_used = (int)((used * 100) / total_harddisk_size);
        if(percent_used >= cri_percent) cout << critical << "\n";
        else if(percent_used < war_percent) cout << ok << "\n";
        else cout << warning << "\n";
    }
    return 0;
}