#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){

    int n;
    cin >> n;
    vector<char> vogais = {'a', 'e', 'i', 'o', 'u'};

    for(int i = 0; i < n; i++){

        int count = 0;
        bool hard = false;
        string sobrenome;
        cin >> sobrenome;

        for(char letter: sobrenome){
            char aux = tolower(letter);

            if(find(vogais.begin(), vogais.end(), aux) == vogais.end()){
                count++;
            } else {
                count = 0;
            }

            if(count == 3){
                hard = true;
                break;
            }
        }

        if(hard){
            cout << sobrenome << " nao eh facil" << endl;
        } else {
            cout << sobrenome << " eh facil" << endl;
        }

    }

    return 0;
}