#include <iostream>

using namespace std;

int main(){

    int n, gifts = 0;
    int restB = 0, restA = 0, restM = 0, restD = 0;

    cin >> n;

    for(int i = 0; i < n; i++){
        string name, group;
        int hours;
        cin >> name >> group >> hours;

        if(group == 'bonecos'){
            gifts += (hours + restB) / 8
            restB = (hours + restB) % 8
        }
        if(group == 'arquitetos'){
            gifts += (hours + restA) / 4
            restA = (hours + restA) % 4
        }
        if(group == 'musicos'){
            gifts += (hours + restM) / 6
            restM = (hours + restM) % 6
        }
        if(group == 'desenhistas'){
            gifts += (hours + restD) / 12
            restD = (hours + restD) % 12
        }
    }

    cout << gifts << endl;

    return 0;
}